# === Stage 64: Add validation for relationship references ===
# Project: PantryMate
def validate_references(items, shopping_lists, usage_logs, restock_alerts):
    """Validate that foreign-key-style references in shopping lists, usage logs, and alerts point to existing items."""
    item_ids = {item["id"] for item in items}
    errors = []

    for sl in shopping_lists:
        if sl["item_id"] not in item_ids:
            errors.append(f"Shopping list references non-existent item: {sl['item_id']}")

    for log in usage_logs:
        if log["item_id"] not in item_ids:
            errors.append(f"Usage log references non-existent item: {log['item_id']}")

    for alert in restock_alerts:
        if alert["item_id"] not in item_ids:
            errors.append(f"Restock alert references non-existent item: {alert['item_id']}")

    return errors
