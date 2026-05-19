"""
SESSION 03 — MULTI-FILE CONTEXT DEMO  (File 2 of 2)
=====================================================
Keep this file open alongside add.py when demoing multiply.py creation.
"""

import logging
from typing import Union

logger = logging.getLogger(__name__)

Number = Union[int, float]


def subtract(a: Number, b: Number) -> Number:
    """
    Return the difference of two numbers.

    Args:
        a: Minuend (the number being subtracted from).
        b: Subtrahend (the number to subtract).

    Returns:
        The arithmetic difference  a - b.

    Examples:
        >>> subtract(10, 3)
        7
        >>> subtract(5.5, 2.0)
        3.5
    """
    logger.debug("subtract called: a=%s, b=%s", a, b)
    result = a - b
    logger.info("subtract(%s, %s) = %s", a, b, result)
    return result


def subtract_many(initial: Number, *numbers: Number) -> Number:
    """
    Subtract an arbitrary sequence of numbers from an initial value.

    Args:
        initial:   Starting value.
        *numbers:  Values to subtract in order.

    Returns:
        initial minus the sum of all subsequent numbers.

    Examples:
        >>> subtract_many(20, 5, 3, 2)
        10
        >>> subtract_many(10)
        10
    """
    if not numbers:
        logger.warning("subtract_many: no values to subtract, returning initial=%s", initial)
        return initial
    result = initial - sum(numbers)
    logger.info("subtract_many(%s, %s) = %s", initial, numbers, result)
    return result
