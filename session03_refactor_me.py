"""
SESSION 03 — COPILOT REFACTORING DEMO
======================================
INSTRUCTOR INSTRUCTIONS:
  This file is intentionally written in a "bad but working" style.
  Use it to demonstrate Copilot's refactoring superpowers:

  DEMO 1 — /simplify  (select get_user_report):
    Shows: extracting magic numbers, simplifying logic, naming

  DEMO 2 — Inline chat  "refactor this to use dataclasses and type hints"
    Shows: modernising legacy-style code

  DEMO 3 — Agent Mode prompt:
    "Refactor this entire file to follow clean code principles:
     extract magic numbers to constants, add type hints to every function,
     replace print() with proper logging, use dataclasses, and add docstrings"

  DEMO 4 — /doc  (select any function without a docstring)
    Shows: AI-generated documentation

  ISSUES IN THIS FILE (15 total):
    - No type hints anywhere
    - Magic numbers (86400, 0.2, 30, etc.)
    - Deeply nested if-else instead of early returns
    - print() used for logging
    - No docstrings
    - Mutable default argument
    - Variable names: x, y, d, tmp, res
    - Global variable as config
    - Duplicate logic copy-pasted in two functions
    - God function (process_everything does too many things)
    - String formatting with % instead of f-strings
    - Bare except
    - Unused imports
    - Class with no __repr__ or __eq__
    - Mixed indentation style
"""

import os, sys, json, math, re, datetime  # noqa: E401  (multiple imports on one line)

# Global "config" — no encapsulation
MAX = 30
DISC = 0.2
SECS = 86400

class order:             # class name not PascalCase
    def __init__(self, i, n, p, q):   # single-char args
        self.i = i       # id
        self.n = n       # name
        self.p = p       # price
        self.q = q       # quantity
        self.d = False   # discounted
        self.ts = None   # timestamp


def calc(o, c):          # no type hints, cryptic names
    res = 0
    if c != None:        # should be 'is not None'
        if c > 0:
            if o.q > 0:
                if o.p > 0:
                    res = o.p * o.q
                    if o.d == True:      # should be just 'if o.d'
                        res = res - (res * DISC)
                    if c > MAX:
                        res = res * 0.95
    return res


def get_user_report(users, start, end):   # no type hints
    tmp = []
    for x in users:
        ok = False
        if x["active"] == True:
            if x["age"] >= 18:
                if x["age"] <= 65:
                    if x["score"] > 50:
                        ok = True
        if ok == True:
            d = {}
            d["id"] = x["id"]
            d["name"] = x["name"]
            d["score"] = x["score"]
            if x["score"] >= 90:
                d["grade"] = "A"
            else:
                if x["score"] >= 75:
                    d["grade"] = "B"
                else:
                    if x["score"] >= 60:
                        d["grade"] = "C"
                    else:
                        d["grade"] = "F"
            # date filter copy-pasted from another function (duplicate logic)
            if start != None and end != None:
                ts = x.get("created_at")
                if ts != None:
                    dt = datetime.datetime.fromisoformat(ts)
                    if dt >= start and dt <= end:
                        tmp.append(d)
            else:
                tmp.append(d)
    print("Found %d users" % len(tmp))   # should be logging, not print
    return tmp


def get_order_report(orders, start, end):   # duplicate of date-filter logic above
    res = []
    for o in orders:
        if o["status"] == "completed":
            # COPY-PASTED DATE FILTER (DRY violation)
            if start != None and end != None:
                ts = o.get("created_at")
                if ts != None:
                    dt = datetime.datetime.fromisoformat(ts)
                    if dt >= start and dt <= end:
                        res.append(o)
            else:
                res.append(o)
    print("Found %d orders" % len(res))
    return res


def process_everything(users, orders, start=None, end=None, extra=[]):  # mutable default
    # God function — does validation, filtering, calculation, formatting, saving
    print("Starting process_everything")
    if users == None or orders == None:
        print("ERROR: bad input")
        return None

    try:
        u_report = get_user_report(users, start, end)
        o_report = get_order_report(orders, start, end)

        summary = {}
        summary["user_count"] = len(u_report)
        summary["order_count"] = len(o_report)

        total = 0
        for o in o_report:
            try:
                total = total + float(o["amount"])
            except:               # bare except
                pass
        summary["total_revenue"] = total

        # magic numbers inline
        if total > 100000:
            summary["tier"] = "platinum"
        else:
            if total > 50000:
                summary["tier"] = "gold"
            else:
                if total > 10000:
                    summary["tier"] = "silver"
                else:
                    summary["tier"] = "bronze"

        for e in extra:
            summary[e] = None     # appending unknown keys with None value

        print("Done. tier=" + summary["tier"])
        return summary
    except Exception as ex:
        print("Error: " + str(ex))
        return None


if __name__ == "__main__":
    sample_users = [
        {"id": 1, "name": "Alice", "active": True,  "age": 28, "score": 92, "created_at": "2024-01-15T10:00:00"},
        {"id": 2, "name": "Bob",   "active": False, "age": 22, "score": 78, "created_at": "2024-02-20T14:30:00"},
        {"id": 3, "name": "Carol", "active": True,  "age": 35, "score": 55, "created_at": "2024-03-01T09:00:00"},
    ]
    sample_orders = [
        {"id": 101, "status": "completed", "amount": "5000.00", "created_at": "2024-01-20T11:00:00"},
        {"id": 102, "status": "pending",   "amount": "2500.50", "created_at": "2024-02-25T16:00:00"},
    ]
    result = process_everything(sample_users, sample_orders)
    print(result)
