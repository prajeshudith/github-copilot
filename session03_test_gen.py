"""
SESSION 03 — TEST GENERATION DEMO
===================================
INSTRUCTOR INSTRUCTIONS:
  1. Open this file and show students the ShoppingCart implementation.
  2. Select the ENTIRE ShoppingCart class.
  3. Open Copilot Chat → type:  /tests
  4. Copilot generates a full pytest suite covering all methods.
  5. Bonus: ask Chat to "add edge case tests for empty cart, negative quantities,
     and items with zero price"
  6. Show how /tests understands the existing code logic including exceptions.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from decimal import Decimal, ROUND_HALF_UP


@dataclass
class CartItem:
    product_id: str
    name: str
    unit_price: Decimal
    quantity: int

    @property
    def subtotal(self) -> Decimal:
        return (self.unit_price * self.quantity).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )


class ShoppingCart:
    """
    In-memory shopping cart.

    Raises:
        ValueError: on invalid quantity or unknown product_id.
        KeyError: when removing a product that is not in the cart.
    """

    TAX_RATE = Decimal("0.18")   # 18% GST

    def __init__(self) -> None:
        self._items: dict[str, CartItem] = {}

    # ── Mutation ──────────────────────────────────────────────────────────────

    def add_item(self, product_id: str, name: str, unit_price: float, quantity: int = 1) -> None:
        """Add a product to the cart or increase its quantity."""
        if quantity <= 0:
            raise ValueError(f"quantity must be positive, got {quantity}")
        if unit_price < 0:
            raise ValueError(f"unit_price must be non-negative, got {unit_price}")
        price = Decimal(str(unit_price))
        if product_id in self._items:
            self._items[product_id].quantity += quantity
        else:
            self._items[product_id] = CartItem(product_id, name, price, quantity)

    def remove_item(self, product_id: str) -> None:
        """Remove a product entirely from the cart."""
        if product_id not in self._items:
            raise KeyError(f"Product '{product_id}' not in cart")
        del self._items[product_id]

    def update_quantity(self, product_id: str, new_quantity: int) -> None:
        """Set an item's quantity. Pass 0 to remove the item."""
        if new_quantity < 0:
            raise ValueError(f"quantity cannot be negative, got {new_quantity}")
        if product_id not in self._items:
            raise KeyError(f"Product '{product_id}' not in cart")
        if new_quantity == 0:
            self.remove_item(product_id)
        else:
            self._items[product_id].quantity = new_quantity

    def clear(self) -> None:
        """Remove all items from the cart."""
        self._items.clear()

    # ── Query ─────────────────────────────────────────────────────────────────

    @property
    def is_empty(self) -> bool:
        return len(self._items) == 0

    @property
    def item_count(self) -> int:
        """Total number of individual units (not unique products) in the cart."""
        return sum(item.quantity for item in self._items.values())

    @property
    def subtotal(self) -> Decimal:
        """Sum of all item subtotals before tax."""
        return sum(
            (item.subtotal for item in self._items.values()),
            Decimal("0.00")
        )

    @property
    def tax(self) -> Decimal:
        return (self.subtotal * self.TAX_RATE).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )

    @property
    def total(self) -> Decimal:
        """Grand total including tax."""
        return self.subtotal + self.tax

    def apply_discount(self, discount_percent: float) -> Decimal:
        """Return the total after applying a percentage discount (0–100)."""
        if not 0 <= discount_percent <= 100:
            raise ValueError(f"discount_percent must be 0–100, got {discount_percent}")
        discount_factor = Decimal(str(1 - discount_percent / 100))
        return (self.total * discount_factor).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )

    def to_dict(self) -> dict:
        """Serialise the cart to a plain dictionary (for JSON responses)."""
        return {
            "items": [
                {
                    "product_id": item.product_id,
                    "name": item.name,
                    "unit_price": str(item.unit_price),
                    "quantity": item.quantity,
                    "subtotal": str(item.subtotal),
                }
                for item in self._items.values()
            ],
            "item_count": self.item_count,
            "subtotal": str(self.subtotal),
            "tax": str(self.tax),
            "total": str(self.total),
        }
