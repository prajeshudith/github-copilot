---
description: "Scaffold a new Flask REST endpoint following project conventions"
---

# New Flask Endpoint

Create a new REST endpoint following our project conventions from copilot-instructions.md.

## Endpoint Specification
Endpoint: ${input:endpoint_description}

## Files to Create/Update
Generate ALL of the following:

### 1. `models/${resource}.py`
- SQLAlchemy 2.x declarative model with `__tablename__`
- All fields typed, with `created_at` and `updated_at` auto-fields
- `to_dict()` method for serialization

### 2. `schemas/${resource}_schema.py`
- Marshmallow Schema for request validation
- Separate `CreateSchema` and `UpdateSchema`
- Custom validators where appropriate

### 3. `repositories/${resource}_repository.py`
- Methods: `save`, `find_by_id`, `find_all`, `delete`
- Use SQLAlchemy `select()` style (2.x)
- Return typed results (model instances or None)

### 4. `services/${resource}_service.py`
- Depends on repository via constructor injection
- Raises typed exceptions from `exceptions.py`
- Full type annotations

### 5. `routes/${resource}_routes.py`
- Flask Blueprint
- Thin handlers: validate → call service → return JSON
- HTTP status codes: 201 Created, 200 OK, 404 Not Found, 400 Bad Request, 422 Unprocessable

### 6. `tests/test_${resource}_service.py`
- Unit tests with mocked repository
- At least: happy path, not-found case, validation error case
- Use `pytest.mark.parametrize` for multiple input scenarios
