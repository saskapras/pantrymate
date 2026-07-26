# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: PantryMate
def upcoming_expiry(items, days_ahead=30):
    """Return items expiring within `days_ahead` days, sorted by date."""
    today = datetime.date.today()
    return [i for i in items if 0 <= (i.expiry_date - today).days <= days_ahead]

def upcoming_restock(items, min_stock=1):
    """Return items that are at or below minimum stock level and need restocking."""
    return [i for i in items if i.quantity is not None and i.quantity < min_stock]
