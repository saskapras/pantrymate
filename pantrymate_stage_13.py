# === Stage 13: Add file save support using a configurable path ===
# Project: PantryMate
import os


def save_pantrymate(config_path: str = "pantrymate_config.json") -> None:
    """Save current pantry configuration to a JSON file."""
    config = {
        "items": items,
        "shopping_list": shopping_list,
        "usage_logs": usage_logs,
        "restock_alerts": restock_alerts,
    }

    if not os.path.exists(config_path):
        with open(config_path, 'w') as f:
            json.dump({"items": [], "shopping_list": [], "usage_logs": [], "restock_alerts": []}, f)


def load_pantrymate(config_path: str = "pantrymate_config.json") -> dict:
    """Load pantry configuration from a JSON file."""
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            return json.load(f)
    else:
        return {"items": [], "shopping_list": [], "usage_logs": [], "restock_alerts": []}


def update_config(config_path: str = "pantrymate_config.json") -> None:
    """Save updated configuration to the file."""
    with open(config_path, 'w') as f:
        json.dump({"items": items, "shopping_list": shopping_list, "usage_logs": usage_logs, "restock_alerts": restock_alerts}, f)
