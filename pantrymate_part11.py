# === Stage 11: Add JSON export for the current application state ===
# Project: PantryMate
def export_state():
    """Export current pantry state to a JSON string."""
    import json
    data = {
        "items": [
            {
                "id": item.id,
                "name": item.name,
                "quantity": item.quantity,
                "expiry_date": item.expiry_date.isoformat() if hasattr(item.expiry_date, 'isoformat') else str(item.expiry_date),
                "unit": item.unit,
            } for item in pantry.get("items", [])
        ],
        "shopping_lists": [
            {
                "id": sl.id,
                "name": sl.name,
                "items": [{"item_id": li.item_id, "quantity": li.quantity} for li in sl.items],
            } for sl in pantry.get("shopping_lists", [])
        ],
        "usage_logs": [
            {
                "id": log.id,
                "date": log.date.isoformat() if hasattr(log.date, 'isoformat') else str(log.date),
                "item_id": log.item_id,
                "quantity_used": log.quantity_used,
            } for log in pantry.get("usage_logs", [])
        ],
    }
    return json.dumps(data, indent=2)
