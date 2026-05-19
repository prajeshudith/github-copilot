# Common Python Code Quality Issues & Fixes

## Syntax Errors

### Missing Colon After Function Definition
**Issue:**
```python
def my_function(x)  # ❌ Missing colon
    return x * 2
```

**Fix:**
```python
def my_function(x):  # ✅ Colon added
    return x * 2
```

---

## Type Hints

### Missing Function Type Hints
**Issue:**
```python
def add(a, b):  # ❌ No type hints
    return a + b
```

**Fix:**
```python
def add(a: int, b: int) -> int:  # ✅ Type hints added
    return a + b
```

### Common Type Hints
```python
def process_data(name: str, age: int, scores: list[float]) -> bool:
    """Process user data."""
    return True
```

---

## Docstrings

### Missing Module Docstring
**Issue:**
```python
# sum.py
def add(x, y):
    return x + y
```

**Fix:**
```python
"""Module for arithmetic operations."""

def add(x: int, y: int) -> int:
    """Add two numbers."""
    return x + y
```

### Missing Function Docstring
**Issue:**
```python
def calculate(a, b, op):
    return op(a, b)
```

**Fix:**
```python
def calculate(a: float, b: float, op: callable) -> float:
    """Calculate the result of applying operation to two numbers.
    
    Args:
        a: The first operand.
        b: The second operand.
        op: The operation function to apply.
    
    Returns:
        The result of the operation.
    """
    return op(a, b)
```

---

## Naming Conventions

### PEP 8 Naming Standards
| Type | Convention | Example |
|------|-----------|---------|
| Functions | `lowercase_with_underscores` | `calculate_total()` |
| Classes | `PascalCase` | `DataProcessor` |
| Constants | `UPPERCASE_WITH_UNDERSCORES` | `MAX_RETRIES = 3` |
| Private members | Leading underscore | `_internal_data` |

### Bad Naming
```python
def calc_val(X, Y):  # ❌ Unclear, inconsistent
    return X + Y

myVar = 100  # ❌ Not constant case
```

### Good Naming
```python
def calculate_total(subtotal: float, tax: float) -> float:  # ✅ Clear, descriptive
    return subtotal + tax

MAX_RETRIES = 3  # ✅ Constants in UPPER_CASE
```

---

## Code Organization

### Bad Organization
```python
# ❌ No structure, everything mixed
import os
def foo():
    pass
import sys
def bar():
    pass
```

### Good Organization
```python
# ✅ Module docstring first
"""Data processing utilities."""

# ✅ Imports grouped
import os
import sys

# ✅ Functions/classes
def foo() -> None:
    """Do something."""
    pass

def bar() -> None:
    """Do something else."""
    pass
```

---

## Unused Code

### Unused Imports
**Issue:**
```python
import os  # ❌ Never used
import sys

print(sys.version)
```

**Fix:**
```python
import sys  # ✅ Removed unused import

print(sys.version)
```

### Unused Variables
**Issue:**
```python
def process_data(name, age):  # ❌ 'age' unused
    return name.upper()
```

**Fix:**
```python
def process_data(name):  # ✅ Removed unused parameter
    return name.upper()
```

---

## PEP 8 Style Issues

### Line Length
- **Max 79 characters** for code, 72 for docstrings/comments
- Split long lines using parentheses or line continuation

### Spacing
```python
# ❌ Bad spacing
x=1+2
dict1={'a':1,'b':2}

# ✅ Good spacing
x = 1 + 2
dict1 = {'a': 1, 'b': 2}
```

### Blank Lines
- **Two blank lines** between top-level functions/classes
- **One blank line** between methods inside a class
