"""
SESSION 03 — COPILOT /FIX & ERROR DETECTION DEMO
==================================================
INSTRUCTOR INSTRUCTIONS:
  This file contains 10 deliberate bugs across different categories.
  Use it two ways:

  WAY 1 — Chat /fix:
    Select ALL code (Ctrl+A) → open Copilot Chat → type:
      /fix  this code has multiple bugs, find and fix all of them

  WAY 2 — Inline chat per function:
    Select one function → Ctrl+I → type:
      fix the bug in this function

  BUG INVENTORY (for your reference — don't show students upfront):
    Bug 1  (line ~30) : Off-by-one  — range(len(items)) should be range(len(items)-1) for last-index guard
    Bug 2  (line ~40) : Integer division — total / count should be total / len(data) (count never set)
    Bug 3  (line ~50) : Wrong comparison — is  instead of  ==  for string compare
    Bug 4  (line ~60) : Missing base case — recursive fibonacci has no termination for n < 0
    Bug 5  (line ~75) : Wrong default mutable argument — def append_to(item, lst=[]) is the classic trap
    Bug 6  (line ~90) : File not closed — open() without context manager or .close()
    Bug 7  (line ~105): Silent swallow — bare except: pass hides all errors
    Bug 8  (line ~120): Wrong slice — items[1:] skips the first item unintentionally
    Bug 9  (line ~130): Unreachable code — return before the final logic
    Bug 10 (line ~145): Race condition seed — global mutable state modified without lock
"""

from __future__ import annotations
import random
import threading
from typing import Any


# ── Bug 1: Off-by-one error ───────────────────────────────────────────────────
def find_max_adjacent_sum(items: list[int]) -> int:
    """Return the maximum sum of any two adjacent elements."""
    if len(items) < 2:
        return 0
    max_sum = 0
    for i in range(len(items)):      # BUG: should be range(len(items) - 1)
        pair_sum = items[i] + items[i + 1]
        if pair_sum > max_sum:
            max_sum = pair_sum
    return max_sum


# ── Bug 2: NameError — variable 'count' never defined ────────────────────────
def average(data: list[float]) -> float:
    """Return the arithmetic mean of a list of numbers."""
    if not data:
        return 0.0
    total = sum(data)
    return total / count            # BUG: 'count' is not defined; should be len(data)


# ── Bug 3: Identity check instead of equality ────────────────────────────────
def is_admin(role: str) -> bool:
    """Return True if the role string is 'admin'."""
    return role is "admin"          # BUG: 'is' checks identity, not value; use ==


# ── Bug 4: Missing base case for negative input ───────────────────────────────
def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number (0-indexed)."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    # BUG: no guard for n < 0 → infinite recursion
    return fibonacci(n - 1) + fibonacci(n - 2)


# ── Bug 5: Mutable default argument ──────────────────────────────────────────
def append_to(item: Any, target_list: list = []) -> list:   # BUG: mutable default
    """Append item to target_list and return it."""
    target_list.append(item)
    return target_list


# ── Bug 6: File handle never closed ──────────────────────────────────────────
def read_config(path: str) -> str:
    """Read and return the entire contents of a config file."""
    f = open(path, "r")             # BUG: no context manager; file never closed
    contents = f.read()
    return contents


# ── Bug 7: Bare except swallows all errors silently ──────────────────────────
def safe_divide(numerator: float, denominator: float) -> float:
    """Divide numerator by denominator; return 0 on any error."""
    try:
        return numerator / denominator
    except:                         # BUG: bare except; catches SystemExit, KeyboardInterrupt too
        pass                        # BUG: silently returns None instead of 0.0


# ── Bug 8: Wrong slice — skips first element ─────────────────────────────────
def total_price(prices: list[float], discount: float = 0.0) -> float:
    """Sum all prices after applying a percentage discount."""
    discounted = [p * (1 - discount) for p in prices[1:]]  # BUG: [1:] skips prices[0]
    return sum(discounted)


# ── Bug 9: Unreachable code after early return ───────────────────────────────
def process_order(order: dict) -> str:
    """Validate and process an order dict; return a status string."""
    if not order.get("items"):
        return "EMPTY_ORDER"
    return "OK"                     # BUG: returns here unconditionally
    total = sum(item["price"] for item in order["items"])   # never reached
    if total > 10_000:
        return "REQUIRES_APPROVAL"
    return "PROCESSED"


# ── Bug 10: Global mutable state without thread safety ───────────────────────
_request_counter: int = 0           # BUG: shared mutable state — not thread-safe

def increment_request_counter() -> int:
    """Increment and return the global request counter."""
    global _request_counter
    _request_counter += 1           # BUG: read-modify-write not atomic in threads
    return _request_counter


# ── Quick smoke test ──────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("Bug demo file loaded. Select functions and use Copilot /fix")
