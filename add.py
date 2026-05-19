"""
SESSION 03 — MULTI-FILE CONTEXT DEMO  (File 1 of 2)
=====================================================
INSTRUCTOR INSTRUCTIONS:
  1. Open BOTH add.py AND subtract.py in VS Code (keep both tabs open).
  2. Create a NEW empty file called  multiply.py  in the same folder.
  3. In multiply.py, type only the module docstring and the first line:
         def multiply(
  4. Watch Copilot read the pattern from these two open files and
     auto-complete multiply() with the SAME style, docstring format,
     error handling, and logging — without you writing anything.
  5. Then try divide.py for extra demo punch.
"""

import logging
from typing import Union

logger = logging.getLogger(__name__)

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """
    Return the sum of two numbers.

    Args:
        a: First operand (int or float).
        b: Second operand (int or float).

    Returns:
        The arithmetic sum  a + b.

    Examples:
        >>> add(3, 4)
        7
        >>> add(1.5, 2.5)
        4.0
    """
    logger.debug("add called: a=%s, b=%s", a, b)
    result = a + b
    logger.info("add(%s, %s) = %s", a, b, result)
    return result


def add_many(*numbers: Number) -> Number:
    """
    Return the sum of an arbitrary number of values.

    Args:
        *numbers: Variable-length sequence of int or float.

    Returns:
        The total sum of all supplied numbers (0 if none given).

    Examples:
        >>> add_many(1, 2, 3, 4)
        10
        >>> add_many()
        0
    """
    if not numbers:
        logger.warning("add_many called with no arguments — returning 0")
        return 0
    total = sum(numbers)
    logger.info("add_many%s = %s", numbers, total)
    return total
