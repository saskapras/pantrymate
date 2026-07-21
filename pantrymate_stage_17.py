# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: PantryMate
def dry_run_mode():
    """Toggle dry-run mode: commands mutate state only if enabled."""
    global _DRY_RUN
    _DRY_RUN = True  # Example toggle; in real usage, read from config or CLI flag
    print("[Dry Run] Mutations will not be applied. All operations are simulated.")

def simulate_add_item(item_name, quantity, expiry_date):
    """Simulate adding an item to the pantry without modifying state."""
    return {"action": "add", "item": item_name, "quantity": quantity, "expiry": expiry_date, "status": "simulated"}

def simulate_remove_item(item_name, quantity=1):
    """Simulate removing an item from the pantry without modifying state."""
    return {"action": "remove", "item": item_name, "quantity": quantity, "status": "simulated"}

def simulate_update_usage_log(item_name, user_id=None, timestamp=None):
    """Simulate updating a usage log entry without modifying state."""
    return {"action": "update_log", "item": item_name, "user": user_id, "time": timestamp, "status": "simulated"}
