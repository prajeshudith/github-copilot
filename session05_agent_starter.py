"""
SESSION 05 — AGENT MODE DEMO STARTER
======================================
INSTRUCTOR INSTRUCTIONS:
  This is a minimal Flask skeleton. Use it as the starting point for
  the Agent Mode live demo. Open Copilot Chat → Agent Target → Local.

  DEMO PROMPT TO USE:
  ─────────────────────────────────────────────────────────────────────
  "Using this Flask app as a base, build a complete Task Management API:

  1. Task model (dataclass): id, title, description, status (todo/in_progress/done),
     priority (low/medium/high), created_at, due_date (optional)

  2. In-memory TaskRepository with methods:
     save, find_by_id, find_all, find_by_status, delete

  3. Flask routes:
     POST   /tasks            → create task
     GET    /tasks            → list all (filter by ?status= and ?priority=)
     GET    /tasks/<id>       → get one
     PATCH  /tasks/<id>       → update status or priority
     DELETE /tasks/<id>       → delete

  4. Input validation using Marshmallow or manual validation
  5. Consistent JSON error responses {error: str, code: int}
  6. pytest tests for every endpoint (happy path + error cases)
  7. Run the tests at the end and fix any failures"
  ─────────────────────────────────────────────────────────────────────

  WATCH FOR:
    • Agent reads this file, understands the Flask setup
    • Agent creates: models.py, repository.py, routes.py, errors.py, test_api.py
    • Agent installs packages (pip install flask marshmallow pytest)
    • Agent runs pytest and self-corrects any failures
"""

from flask import Flask, jsonify

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
