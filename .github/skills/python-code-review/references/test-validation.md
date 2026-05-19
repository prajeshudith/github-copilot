# Test Validation Guide

## Running Tests

### Using pytest (Recommended)

```bash
# Run all tests in current directory
python -m pytest -v

# Run specific test file
python -m pytest test.py -v

# Run specific test function
python -m pytest test.py::test_addition_positive_numbers -v

# Run with coverage report
python -m pytest --cov=.
```

### Using unittest

```bash
# Run all tests
python -m unittest discover

# Run specific file
python -m unittest test.py

# Run specific test
python -m unittest test.TestAddition.test_positive_numbers
```

## Understanding Test Output

### Success Output
```
test.py::test_addition_positive_numbers PASSED        [  8%]
test.py::test_addition_negative_numbers PASSED        [ 16%]
...
================== 12 passed in 0.08s ====================
```
✅ All tests passed - safe to commit

### Failure Output
```
test.py::test_addition_positive_numbers FAILED        [  8%]
...
AssertionError: assert 8 == 9

================== 1 failed, 11 passed in 0.10s ==========
```
❌ Tests failed - review changes before committing

## Test-Driven Review Process

1. **Run tests BEFORE changes**
   ```bash
   python -m pytest test.py -v
   ```
   - Baseline to verify tests pass initially
   - Ensures changes didn't inadvertently break tests

2. **Make code improvements**
   - Fix syntax errors
   - Add type hints
   - Improve docstrings
   - Refactor code

3. **Run tests AFTER changes**
   ```bash
   python -m pytest test.py -v
   ```
   - Verify all tests still pass
   - Ensure no functionality was broken

4. **Validate imports work**
   ```bash
   python -c "from module_name import function_name; print('Import successful')"
   ```

## Common Test Issues

### Import Errors During Tests
**Problem:** `ModuleNotFoundError: No module named 'add'`

**Solution:**
```bash
# Run from the root directory where modules are located
cd /path/to/project/root
python -m pytest test/ -v  # Use -m for proper path handling
```

### Tests Not Discovered
**Problem:** `no tests collected`

**Cause:** 
- Test file not named `test_*.py` or `*_test.py`
- Test functions not named `test_*`

**Solution:**
```python
# ✅ Correct naming
def test_addition():
    assert add(2, 2) == 4

# ❌ Incorrect naming
def check_addition():  # Won't be discovered
    assert add(2, 2) == 4
```

### Assertion Format

With pytest, use simple `assert` statements:
```python
# ✅ Pytest style
def test_add():
    assert add(2, 2) == 4

# ❌ Don't use unittest syntax with pytest
def test_add():
    self.assertEqual(add(2, 2), 4)  # Wrong!
```

## Success Criteria for Code Review

✅ **All tests pass**: No failures or errors  
✅ **No import errors**: Modules import successfully  
✅ **Proper test format**: Using pytest conventions  
✅ **No regressions**: Existing tests still pass  
✅ **Coverage maintained**: New code has corresponding tests
