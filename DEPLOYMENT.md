
# AI Resume Analyzer – Railway Deployment

## 1. Project Overview

AI Resume Analyzer is a Frappe v15 application that analyzes uploaded PDF resumes and generates AI-powered candidate summaries.

## 2. Technology Stack

- Frappe Framework v15
- Python
- MariaDB
- Redis
- Groq API
- OpenRouter API
- Docker
- Railway

## 3. Application Location

The custom Frappe application is located at:

`w2d3-ai-resume-analysis/frappe_app/`

App name: `resume_analyzer`

## 4. Deployment Platform

The application is intended to be deployed on Railway using Docker.

## 5. Required Services

- Frappe application service
- MariaDB database
- Redis cache and queue services
- Background worker
- Scheduler
- Socket.IO service

## 6. Environment Configuration

The deployment requires database credentials, Redis connection URLs, Frappe site configuration, administrator credentials, and AI provider API keys.

Never commit passwords or API keys to GitHub.

## 7. Deployment Status

Deployment configuration and testing are in progress.

## 8. Application Testing

1. Open the deployed Frappe site.
2. Open the Job Applicant form.
3. Upload a PDF resume.
4. Generate the AI resume summary.
5. Verify that the generated summary is saved.

## 9. Developer

Prachi Ruikar

Cynaris Solutions – Full Stack Development Internship
