# === Stage 28: Add overdue item detection based on due dates ===
# Project: PantryMate
def detect_overdue_items(items: list[dict]) -> list[tuple[dict, str]]:
    """Return a list of (item_dict, reason) for items past their due date."""
    overdue = []
    today = datetime.date.today()
    for item in items:
        if "expiry_date" in item and item["expiry_date"] < today:
            days_left = (today - item["expiry_date"]).days
            overdue.append((item, f"{days_left} day(s) expired"))
        elif "restock_date" in item and item["restock_date"] < today:
            days_left = (today - item["restock_date"]).days
            overdue.append((item, f"{days_left} day(s) past restock target"))
    return overdue

def format_overdue_report(overdue_items: list[tuple[dict, str]]) -> str:
    """Generate a human-readable report of overdue items."""
    if not overdue_items:
        return "All items are current. No overdue alerts."
    lines = ["Overdue Items Report:\n"]
    for item, reason in overdue_items:
        name = item.get("name", "?")
        qty = item.get("quantity", 0)
        lines.append(f"  - {name}: {reason} (remaining: {qty})")
    return "\n".join(lines)

def get_days_until_expiry(items: list[dict]) -> dict[str, int]:
    """Return a dictionary mapping item name to days remaining until expiry."""
    result = {}
    today = datetime.date.today()
    for item in items:
        if "expiry_date" in item and item["expiry_date"] > today:
            days = (item["expiry_date"] - today).days
            result[item.get("name", "?")] = max(0, days)
    return result

if __name__ == "__main__":
    sample_items = [
        {"name": "Milk", "quantity": 2, "expiry_date": datetime.date.today() + datetime.timedelta(days=5)},
        {"name": "Yogurt", "quantity": 1, "expiry_date": datetime.date.today() - datetime.timedelta(days=3)},
        {"name": "Bread", "quantity": 4, "restock_date": datetime.date.today() - datetime.timedelta(days=7)},
    ]
    overdue = detect_overdue_items(sample_items)
    print(format_overdue_report(overdue))
