# === Stage 58: Add bulk update behavior for selected records ===
# Project: PantryMate
def bulk_update(items, field_name, value):
    """Update multiple items in a list by setting a common field to a given value."""
    for item in items:
        if field_name in item and not isinstance(item[field_name], dict):
            item[field_name] = value
    return items
