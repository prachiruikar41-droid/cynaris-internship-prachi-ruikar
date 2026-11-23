# Week 2 Day 4 — Debugging & Performance Sprint

## 1. Issue Observed

The Frappe worker logs showed the following error:

`redis.exceptions.ConnectionError: Error 111 connecting to 127.0.0.1:11000. Connection refused.`

## 2. Investigation

- Checked Frappe worker error logs.
- Checked Redis processes using `ps`.
- Found that Redis was running on port 6379, but the required bench Redis services were not running.
- Checked the Procfile and Redis configuration files.
- Confirmed that redis_queue uses port 11000 and redis_cache uses port 13000.

## 3. Root Cause

The Frappe bench services were not running, so the Redis Queue and Cache services were unavailable.

## 4. Resolution

- Started the Frappe services using `bench start`.
- Verified Redis Queue using `redis-cli -p 11000 ping`.
- Verified Redis Cache using `redis-cli -p 13000 ping`.
- Both commands returned `PONG`.

## 5. Testing

- Opened the Frappe application successfully.
- Opened the Job Applicant record.
- Generated the AI Resume Summary successfully.
- Refreshed the page and verified that the generated summary was still present.

## 6. Result

The Redis connectivity issue was resolved by starting the required bench services. The AI Resume Analyzer feature worked successfully after recovery.

No application code changes were required for this issue.

## 7. Evidence

- `screenshots/01-redis-connection-error.png`
- `screenshots/02-ai-summary-after-refresh.png`

## 8. Pending Review

CIA QA Engineer Mode and Code Mode reviews are pending because CIA was unavailable during this work.
