# AI Resume Analyzer - Testing Log

## Test Cases

| Test Case | Expected Result | Status |
|---|---|---|
| Valid PDF with Groq | AI summary generated successfully | PASS |
| Groq failure | OpenRouter fallback generates summary | PASS |
| Missing resume | Generate button is unavailable | PASS |
| Invalid JPG attachment | Friendly PDF validation error displayed | PASS |
| Summary persistence | Generated summary remains after page refresh | PASS |

## Test Environment

- Frappe Framework
- Frappe HRMS
- Groq API
- OpenRouter API
- Python and JavaScript

## Notes

API credentials are stored in Frappe site configuration and are not included in this repository.
