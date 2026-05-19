---
name: python-code-review
description: 'Review and improve Python code quality. Use when: refactoring code, enforcing code standards, adding type hints and docstrings, fixing syntax errors, or ensuring tests pass.'
user-invocable: true
---

# Python Code Review Skill

## When to Use

- **Refactoring existing Python code** to improve quality
- **Enforcing code standards** across the project
- **Adding missing type hints** and docstrings
- **Fixing syntax errors** and style issues
- **Validating changes** don't break tests

## Review Checklist

This skill performs a comprehensive review covering:

### 1. Syntax & Errors
- Missing colons, parentheses, or brackets
- Import statements are valid
- No undefined variables or functions

### 2. Type Hints
- Function parameters have type annotations
- Return types are specified
- Type hints follow PEP 484 conventions

### 3. Documentation
- Module-level docstrings present
- Functions have docstrings with Args and Returns
- Docstrings follow PEP 257 format
- Inline comments explain complex logic

### 4. Code Style
- PEP 8 compliance (naming, spacing, line length)
- Consistent formatting
- No unused imports or variables
- Proper naming conventions (snake_case for functions)

### 5. Testing
- All unit tests pass after changes
- Changes don't break existing functionality

## Step-by-Step Procedure

### Step 1: Identify Issues
- Read the Python files
- Check for syntax errors (missing colons, parentheses)
- Look for missing type hints
- Assess documentation quality
- Evaluate code style and naming conventions

### Step 2: Plan Fixes
- Prioritize critical issues (syntax errors first)
- Group related changes (e.g., all type hints together)
- Ensure fixes don't overlap or cause conflicts

### Step 3: Apply Fixes
- Fix syntax errors first
- Add or improve type hints
- Add comprehensive docstrings
- Improve variable/function names if needed
- Format code according to PEP 8

### Step 4: Validate Changes
- Run unit tests: `pytest test.py -v` or `python -m pytest test/ -v`
- Verify all tests pass
- Ensure no new errors introduced
- Check imports work correctly

### Step 5: Summary
- Report all issues found
- Show improvements made
- Confirm test results

## Example Trigger Phrases

- "Review this Python code and fix issues"
- "Improve code quality for these Python files"
- "Add type hints and docstrings"
- "Make sure this Python code passes PEP 8"
- "Review and fix the Python code using the python-code-review skill"

## Key Tools Used

- `read_file`: Examine Python source code
- `replace_string_in_file` / `multi_replace_string_in_file`: Apply fixes
- `run_in_terminal`: Execute `pytest` for validation
- `get_errors`: Identify syntax and style issues

## Reference: PEP 8 Quick Guide

- Functions: `def function_name(param: str) -> str:`
- Classes: `class ClassName:`
- Constants: `MAX_SIZE = 100`
- Private methods: `def _private_method(self):`

## Reference: PEP 257 Docstring Format

```python
def add_numbers(a: float, b: float) -> float:
    """Add two numbers and return their sum.
    
    Args:
        a: The first number to add.
        b: The second number to add.
    
    Returns:
        The sum of a and b.
    """
    return a + b
```

## Module-Level Docstring

```python
"""Module for mathematical operations."""
```

## Success Criteria

✅ All syntax errors fixed  
✅ Type hints added to functions  
✅ Comprehensive docstrings present  
✅ PEP 8 compliance verified  
✅ All unit tests passing  
✅ Code is readable and maintainable
