# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: PantryMate
from dataclasses import dataclass, field
from datetime import date


@dataclass
class PantryItem:
    name: str
    expiry_date: date
    quantity: float = 1.0
    unit: str = "unit"
    notes: str = ""


@dataclass
class ShoppingListEntry:
    item_name: str
    required_qty: float = 1.0
    added_by: str = "user"
    date_added: date = field(default_factory=date.today)


@dataclass
class UsageLog:
    item_name: str
    quantity_used: float
    used_date: date = field(default_factory=date.today)
    notes: str = ""


@dataclass
class RestockAlert:
    item_name: str
    current_qty: float
    threshold: float
    triggered_date: date = field(default_factory=date.today)


def get_expiry_days_left(item: PantryItem, today: date | None = None) -> int:
    if today is None:
        today = date.today()
    delta = item.expiry_date - today
    return max(0, delta.days)
