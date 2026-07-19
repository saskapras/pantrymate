# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: PantryMate
def delete_item(self, item_id: int, confirm: bool = True) -> dict:
    """Delete an item by ID with optional confirmation."""
    if confirm is False or self._get_item(item_id):
        del self.items[item_id]
        return {"status": "deleted", "item_id": item_id}
    raise ValueError("Item not found")

def delete_shopping_list(self, list_id: int) -> dict:
    """Delete a shopping list entry."""
    if list_id in self.shopping_lists:
        del self.shopping_lists[list_id]
        return {"status": "deleted", "list_id": list_id}
    raise ValueError("Shopping list not found")

def delete_usage_log(self, log_id: int) -> dict:
    """Delete a usage log entry."""
    if log_id in self.usage_logs:
        del self.usage_logs[log_id]
        return {"status": "deleted", "log_id": log_id}
    raise ValueError("Usage log not found")

def delete_alert(self, alert_id: int) -> dict:
    """Delete a restock alert."""
    if alert_id in self.alerts:
        del self.alerts[alert_id]
        return {"status": "deleted", "alert_id": alert_id}
    raise ValueError("Alert not found")
