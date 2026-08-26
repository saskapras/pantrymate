# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: PantryMate
def reset_demo_data(db):
    """Reset all tables to demo state for manual testing."""
    db["items"].clear()
    db["items"].extend([
        {"id": 1, "name": "Milk", "quantity": 2, "unit": "L", "expiry_date": "2025-03-15"},
        {"id": 2, "name": "Eggs", "quantity": 12, "unit": "pcs", "expiry_date": "2025-04-01"},
        {"id": 3, "name": "Flour", "quantity": 5, "unit": "kg", "expiry_date": "2026-01-20"},
    ])
    db["usage_logs"].clear()
    db["usage_logs"].extend([
        {"id": 1, "item_id": 1, "used_qty": 0.5, "date": "2025-01-15"},
        {"id": 2, "item_id": 2, "used_qty": 3, "date": "2025-01-14"},
    ])
    db["shopping_lists"].clear()
    db["shopping_lists"].extend([
        {"id": 1, "item_id": 3, "quantity": 2, "unit": "kg", "status": "pending"},
        {"id": 2, "item_id": 1, "quantity": 1, "unit": "L", "status": "pending"},
    ])
    db["restock_alerts"].clear()
    db["restock_alerts"].extend([
        {"id": 1, "item_id": 1, "alert_date": "2025-02-01", "status": "active"},
        {"id": 2, "item_id": 3, "alert_date": "2025-12-01", "status": "active"},
    ])
    return "Demo data reset"
