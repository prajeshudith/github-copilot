# GitHub Copilot Instructions — Python Backend Course Demo Project
#
# SESSION 08 DEMO: Place this file at  .github/copilot-instructions.md
# Then generate any Python function WITH and WITHOUT this file to compare output.

## Project Stack
- Language: Python 3.12 (use `|` union types, not Optional[X])
- Web framework: Flask 3.x with Blueprints
- Data validation: Marshmallow 3.x schemas
- ORM: SQLAlchemy 2.x with declarative models
- Testing: pytest with pytest-flask and pytest-mock
- Logging: structlog with JSON output in production
- Task queue: Celery with Redis broker

## Code Style Rules
- Use dataclasses or Pydantic models — never raw dicts as return types from service layer
- All functions must have full type annotations (parameters AND return type)
- Use early returns to avoid deep nesting — maximum 2 levels of indentation in business logic
- Never use bare `except:` — always catch specific exceptions
- Never use `print()` for diagnostics — always use `logger = structlog.get_logger()`
- Prefer `pathlib.Path` over `os.path` for file operations

## Architecture Conventions
- Route handlers are THIN: validate input → call service → return JSON response
- All business logic lives in `services/` — routes never touch the database directly
- Database access is ONLY in `repositories/` — services never import SQLAlchemy directly
- Errors: raise custom exceptions from `exceptions.py`; handled in `error_handlers.py`
- Never hardcode config values — always read from environment via `config.py`

## Testing Requirements
- Every public function in `services/` must have at least one unit test
- Use `pytest.mark.parametrize` for data-driven tests
- Mock the repository layer when testing services (never hit a real DB in unit tests)
- Integration tests (hitting the DB) go in `tests/integration/` and are marked `@pytest.mark.integration`

## What NOT to generate
- Do not use Flask-RESTful or Flask-RESTX (we use plain Flask + Marshmallow)
- Do not use SQLAlchemy 1.x style (no `session.query()` — use `select()` statements)
- Do not use `typing.Dict` or `typing.List` — use `dict` and `list` directly (Python 3.9+)
