# === Stage 45: Add restore from backup with validation ===
# Project: PantryMate
def restore_from_backup(self, backup_path: str) -> bool:
        """Restore pantry state from a JSON backup with validation."""
        try:
            import json
            with open(backup_path) as f:
                raw = json.load(f)
            if not isinstance(raw, dict):
                return False
            for key in ("items", "shopping_lists", "usage_logs"):
                if key not in raw or not isinstance(raw[key], list):
                    print(f"Invalid backup: missing or malformed '{key}'.")
                    return False
            self.items = [Item(**i) for i in raw["items"]]
            self.shopping_lists = {k: ShoppingList(**v) for k, v in raw["shopping_lists"].items()}
            self.usage_logs = [UsageLog(**u) for u in raw["usage_logs"]]
        except Exception as e:
            print(f"Restore failed: {e}")
            return False
        return True
