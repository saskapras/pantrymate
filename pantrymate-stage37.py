# === Stage 37: Add recommendations for the next useful action ===
# Project: PantryMate
def suggest_next_action(items, shopping_list):
    """Suggest the next useful action based on current pantry state."""
    if not items:
        return "Add your first item to start tracking!"
    
    expiring_soon = [item for item in items if item.get("expires", None) and _days_until(item["expires"]) <= 7]
    low_stock = [item for item in items if item.get("quantity", 0) < item.get("reorder_threshold", 3)]
    
    if expiring_soon:
        return f"Use or discard these {len(expiring_soon)} items expiring soon: {_get_names(expiring_soon)}."
    if low_stock:
        return f"Restock these low items: {_get_names(low_stock)}."
    if shopping_list and len(shopping_list) > 0:
        return f"You have {len(shopping_list)} item(s) to add to your next shop trip."
    if not expiring_soon and not low_stock and not shopping_list:
        return "Your pantry looks great! Consider adding more items or sharing with friends."

def _days_until(date):
    from datetime import datetime, timedelta
    today = datetime.now().date()
    try:
        target = datetime.strptime(str(date), "%Y-%m-%d").date()
    except ValueError:
        try:
            target = datetime.strptime(str(date), "%m/%d/%Y").date()
        except ValueError:
            return 0
    delta = (target - today).days
    return max(0, delta)

def _get_names(items):
    names = [item.get("name", "Unknown") for item in items]
    return ", ".join(names[:5]) + ("..." if len(names) > 5 else "")
