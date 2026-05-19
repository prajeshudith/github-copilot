"""
SESSION 02 — COMMENT-DRIVEN DEVELOPMENT DEMO
=============================================
INSTRUCTOR INSTRUCTIONS:
  This file has only comments and type stubs. The student types nothing but
  the comments — Copilot generates every implementation.

  DEMO FLOW:
    1. Open this file. Show students only the comments exist.
    2. Place cursor at the end of each comment block.
    3. Press Enter — Copilot generates the full function body.
    4. Press Tab to accept.
    5. Repeat for each function.

  The key point: the MORE detailed your comment, the BETTER the code.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Iterator


@dataclass
class Product:
    sku: str
    name: str
    price: float
    stock: int
    category: str
    created_at: datetime = field(default_factory=datetime.utcnow)


# Step 1: validate that the SKU is non-empty, alphanumeric + dashes only, max 20 chars.
# Raise ValueError with a descriptive message if invalid. Return True if valid.


# Step 2: calculate the discounted price for a product.
# discount_percent is a float between 0 and 100.
# Raise ValueError if discount_percent is outside that range.
# Round the result to 2 decimal places.


# Step 3: filter a list of products to only those in a given category,
# with stock greater than min_stock, and price between min_price and max_price.
# All filter arguments are optional (default: no filtering on that dimension).
# Return a new list — do not modify the input.


# Step 4: apply a bulk discount to every product in a list.
# The discount is tiered based on stock level:
#   stock >= 100  →  5% discount
#   stock >= 50   →  10% discount
#   stock >= 20   →  15% discount
#   stock < 20    →  20% discount (clearance)
# Return a new list of products with updated prices; do not mutate the originals.


# Step 5: generate a paginated iterator over a list of products.
# page is 1-indexed. page_size defaults to 10.
# Yield each product on the requested page.
# Raise IndexError if page is out of range (beyond available pages).


# Step 6: serialize a list of products to a CSV string.
# The header row must be: sku,name,price,stock,category,created_at
# Format created_at as ISO-8601. Escape commas in name/category with quotes.
# Return the full CSV as a single string (not written to file).