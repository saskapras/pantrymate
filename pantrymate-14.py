# === Stage 14: Add file load support with fallback demo data ===
# Project: PantryMate
def load_data(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        pass
    except (json.JSONDecodeError, OSError):
        pass
    demo = {
        "items": [
            {"id": 1, "name": "Milk", "expiry_date": "2025-12-31", "quantity": 2},
            {"id": 2, "name": "Eggs", "expiry_date": "2026-03-15", "quantity": 12}
        ],
        "shopping_lists": [
            {"id": 1, "item_id": 1, "quantity": 1, "status": "pending"}
        ]
    }
    return demo
