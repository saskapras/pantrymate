# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: PantryMate
def update_item(item_id, updates):
    """Update an item's fields from a dict of {field: new_value}."""
    try:
        idx = next(i for i, it in enumerate(items) if it["id"] == item_id)
    except StopIteration:
        print(f"Item '{item_id}' not found; nothing changed.")
        return False

    for field, value in updates.items():
        items[idx][field] = value

    print(f"Updated {len(updates)} field(s) for item {item_id}.")
    return True


def update_shopping_list(shopping_id, updates):
    """Update a shopping-list entry."""
    try:
        idx = next(i for i, sl in enumerate(shopping_lists) if sl["id"] == shopping_id)
    except StopIteration:
        print(f"Shopping list '{shopping_id}' not found; nothing changed.")
        return False

    for field, value in updates.items():
        shopping_lists[idx][field] = value

    print(f"Updated {len(updates)} field(s) for shopping list {shopping_id}.")
    return True


def update_usage_log(log_id, updates):
    """Update a usage-log record."""
    try:
        idx = next(i for i, ul in enumerate(usage_logs) if ul["id"] == log_id)
    except StopIteration:
        print(f"Usage log '{log_id}' not found; nothing changed.")
        return False

    for field, value in updates.items():
        usage_logs[idx][field] = value

    print(f"Updated {len(updates)} field(s) for usage log {log_id}.")
    return True


def update_alerts(alert_id, updates):
    """Update an alert record."""
    try:
        idx = next(i for i, a in enumerate(alerts) if a["id"] == alert_id)
    except StopIteration:
        print(f"Alert '{alert_id}' not found; nothing changed.")
        return False

    for field, value in updates.items():
        alerts[idx][field] = value

    print(f"Updated {len(updates)} field(s) for alert {alert_id}.")
    return True


def update_expiring_items(end_date):
    """Mark items expiring before end_date as 'expiring'."""
    updated = 0
    for item in items:
        if item["expiry_date"] and item["expiry_date"] < end_date and item["status"] != "expired":
            item["status"] = "expiring"
            updated += 1
    print(f"{updated} item(s) marked as expiring.")
    return updated
