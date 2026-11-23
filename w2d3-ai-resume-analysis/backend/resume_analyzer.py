
import frappe
import requests
from pypdf import PdfReader


def call_ai_provider(provider, api_key, model, resume_text):
    """Send resume text to an AI provider and return its summary."""

    if provider == "groq":
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    else:
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:8000",
            "X-Title": "AI Resume Analyzer"
        }

    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are an expert resume analyst. "
                    "Analyze resumes objectively and summarize "
                    "skills, education, projects, experience, "
                    "strengths and areas for improvement. "
                    "Do not invent information."
                )
            },
            {
                "role": "user",
                "content": (
                    "Analyze this resume and provide a clear, "
                    "professional summary:\n\n" + resume_text[:12000]
                )
            }
        ],
        "temperature": 0.3
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=60
    )
    response.raise_for_status()

    result = response.json()
    summary = result["choices"][0]["message"]["content"].strip()

    if not summary:
        raise ValueError("Empty AI response")

    return summary


@frappe.whitelist()
def generate_resume_summary(applicant_id):
    """Generate and save an AI summary for a Job Applicant."""

    try:
        applicant = frappe.get_doc("Job Applicant", applicant_id)
        applicant.check_permission("write")

        if not applicant.resume_attachment:
            frappe.throw("Please upload a resume PDF first.")

        file_doc = frappe.get_doc(
            "File",
            {
                "file_url": applicant.resume_attachment,
                "attached_to_doctype": "Job Applicant",
                "attached_to_name": applicant.name
            }
        )

        file_path = file_doc.get_full_path()
        if not file_path.lower().endswith(".pdf"):
            frappe.throw("Please upload a valid PDF file.")
        reader = PdfReader(file_path)

        resume_text = "\n".join(
            page.extract_text() or "" for page in reader.pages
        ).strip()

        if not resume_text:
            frappe.throw("Could not extract text from this PDF.")

        groq_key = frappe.conf.get("groq_api_key")
        openrouter_key = frappe.conf.get("openrouter_api_key")

        if not groq_key and not openrouter_key:
            frappe.throw(
                "AI API keys are not configured. Please contact the administrator."
            )

        summary = None
        provider_used = None

        if groq_key:
            try:
                summary = call_ai_provider(
                    "groq",
                    groq_key,
                    frappe.conf.get(
                        "groq_model",
                        "llama-3.3-70b-versatile"
                    ),
                    resume_text
                )
                provider_used = "Groq"

            except Exception as e:
                detail = f"{type(e).__name__}: {e}"
                if isinstance(e, requests.HTTPError) and e.response is not None:
                    detail += f"\nHTTP status: {e.response.status_code}\nResponse: {e.response.text[:1000]}"
                frappe.log_error(
                    title="Groq Resume Analysis Failed",
                    message=detail
                )

        if not summary and openrouter_key:
            try:
                summary = call_ai_provider(
                    "openrouter",
                    openrouter_key,
                    frappe.conf.get(
                        "openrouter_model",
                        "openai/gpt-oss-20b:free"
                    ),
                    resume_text
                )
                provider_used = "OpenRouter"

            except Exception as e:
                detail = f"{type(e).__name__}: {e}"
                if isinstance(e, requests.HTTPError) and e.response is not None:
                    detail += f"\nHTTP status: {e.response.status_code}\nResponse: {e.response.text[:1000]}"
                frappe.log_error(
                    title="OpenRouter Resume Analysis Failed",
                    message=detail
                )

        if not summary:
            frappe.throw(
                "AI resume analysis failed. Please check API configuration and try again."
            )

        applicant.ai_resume_summary = summary
        applicant.save()

        return {
            "success": True,
            "summary": summary,
            "provider": provider_used
        }

    except frappe.DoesNotExistError:
        frappe.throw("Job Applicant record not found.")

    except Exception:
        frappe.log_error(
            title="AI Resume Analyzer Error",
            message=frappe.get_traceback()
        )
        raise
