# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: PantryMate
def seed_demo_data(items, shopping_lists, usage_logs, alerts):
    """Populate empty collections with deterministic sample data."""
    sample_items = [
        {"id": 1, "name": "Rice", "quantity": 5, "unit": "kg", "expiry_date": "2026-03-15"},
        {"id": 2, "name": "Olive Oil", "quantity": 0.75, "unit": "L", "expiry_date": "2025-12-01"},
        {"id": 3, "name": "Tomato Sauce", "quantity": 3, "unit": "cans", "expiry_date": "2025-09-20"},
        {"id": 4, "name": "Pasta", "quantity": 2, "unit": "kg", "expiry_date": "2026-06-10"},
        {"id": 5, "name": "Chili Powder", "quantity": 1.5, "unit": "kg", "expiry_date": "2025-08-05"},
    ]
    for i, item in enumerate(sample_items):
        items.append(item)

    sample_shopping = [
        {"id": 1, "item_name": "Quinoa", "quantity_needed": 1},
        {"id": 2, "item_name": "Lemon", "quantity_needed": 4},
        {"id": 3, "item_name": "Black Beans", "quantity_needed": 2},
    ]
    for i, sl in enumerate(sample_shopping):
        shopping_lists.append(sl)

    sample_logs = [
        {"id": 1, "item_name": "Rice", "used_qty": 0.5, "date": "2025-08-20"},
        {"id": 2, "item_name": "Olive Oil", "used_qty": 0.1, "date": "2025-08-22"},
        {"id": 3, "item_name": "Tomato Sauce", "used_qty": 1, "date": "2025-08-25"},
    ]
    for i, log in enumerate(sample_logs):
        usage_logs.append(log)

    sample_alerts = [
        {"id": 1, "item_name": "Chili Powder", "message": "Low stock, consider restocking"},
        {"id": 2, "item_name": "Olive Oil", "message": "Expiry approaching within 30 days"},
    ]
    for i, alert in enumerate(sample_alerts):
        alerts.append(alert)

    return items, shopping_lists, usage_logs, alerts
