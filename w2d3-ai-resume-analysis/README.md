# AI Resume Analysis

## Project Overview

AI-powered resume analysis integrated with the Frappe HR Job Applicant module. The application extracts text from uploaded PDF resumes and generates AI-based candidate summaries.

## Features

- Generate AI-based resume summaries from uploaded PDF resumes.
- Groq API as the primary AI provider.
- OpenRouter API as a fallback provider.
- Automatically switch to OpenRouter if Groq fails.
- Save generated summaries in the Job Applicant record.
- Display generated summaries on the Job Applicant form.
- Validate resume file format.
- Handle missing resumes and API failures with user-friendly error messages.
- Log backend errors for debugging.

## Technology Stack

- Python
- JavaScript
- Frappe Framework
- Frappe HRMS
- PyPDF
- Groq API
- OpenRouter API

## Project Structure

```text
w2d3-ai-resume-analysis/
│
├── backend/
│   └── resume_analyzer.py
│
├── frontend/
│   └── job_applicant.js
│
├── docs/
│
├── .gitignore
└── README.md
```

## Implementation Details

### Backend
- Extracts text from PDF resumes using PyPDF.
- Sends resume content to Groq for AI analysis.
- Uses OpenRouter as a fallback provider.
- Saves the generated summary to the Job Applicant record.

### Frontend
- Adds a "Generate AI Resume Summary" button to the Job Applicant form.
- Calls the backend method using `frappe.call`.
- Displays the generated summary and provider information.

## Security

- API keys are stored securely in Frappe site configuration.
- API keys and credentials must never be committed to GitHub.
- `.env` files and sensitive configuration files must be excluded from version control.

## Testing Completed

- Successful resume PDF analysis using Groq.
- Successful fallback testing using OpenRouter.
- Missing resume validation.
- Invalid file format validation.
- Generated summary persistence after page refresh.

## Project Status

Core implementation, Frappe integration, and primary testing completed.

Documentation, GitHub commits, and final project demonstration are in progress.