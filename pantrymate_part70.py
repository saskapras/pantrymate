# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: PantryMate
import json, sys

def clear_state():
    """Reset all stored data to empty defaults."""
    data = {
        "items": [],
        "shopping_lists": [],
        "usage_logs": [],
        "restock_alerts": [],
        "config": {"last_updated": None}
    }
    with open("pantrymate_data.json", "w") as f:
        json.dump(data, f, indent=2)
    print("PantryMate state cleared successfully.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--confirm":
        clear_state()
    else:
        print("Usage: python pantrymate.py clear_state --confirm")
        sys.exit(1)
