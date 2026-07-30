# === Stage 43: Add CSV import for the primary record type ===
# Project: PantryMate
import csv, os
from datetime import date
from pantrymate.items import PantryItem


def import_items_csv(source_path):
    """Read a CSV with columns: name, quantity, unit, expiry_date (YYYY-MM-DD)."""
    if not source_path or not os.path.isfile(source_path):
        raise FileNotFoundError(f"CSV file not found: {source_path}")

    items = []
    with open(source_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = (row.get('name') or '').strip()
            if not name:
                continue
            expiry_str = (row.get('expiry_date') or '').strip()
            try:
                expiry = date.fromisoformat(expiry_str)
            except ValueError:
                expiry = None

            qty = int(row.get('quantity', 0))
            unit = (row.get('unit') or 'piece').strip().lower()
            items.append(PantryItem(name, qty, expiry=expiry, unit=unit))

    return items
