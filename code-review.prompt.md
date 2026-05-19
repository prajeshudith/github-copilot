---
description: "Full code review: security, quality, and test coverage gaps"
---

# Code Review — #file

Please review the attached file and structure your response exactly as follows:

## 🔴 Security Issues
For each issue provide: line number, vulnerability type, severity (Critical/High/Medium/Low), and a fixed code snippet.
Check for: SQL injection, hardcoded secrets, insecure deserialization, path traversal, unvalidated input, OWASP Top 10.

## 🟡 Code Quality Issues
Check for: naming clarity, DRY violations, SOLID principle breaches, cyclomatic complexity > 10, mutable defaults, bare excepts.

## 🟢 Missing Test Coverage
For each public function that has no test, suggest a test case including: function name, test scenario, expected outcome.

## ✅ Summary
Provide: overall risk level, top 3 priority fixes, and estimated effort in developer-hours.
