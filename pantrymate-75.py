# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: PantryMate
import datetime
import re

def validate_pantry(pantry):
    warnings = []
    errors = []
    now = datetime.datetime.now()
    for item in pantry.items:
        if item.quantity <= 0:
            errors.append(f"Item '{item.name}' has zero or negative quantity.")
        if item.expiry_date and item.expiry_date < now:
            days_left = (item.expiry_date - now).days
            if days_left < 0:
                warnings.append(f"Item '{item.name}' is expired ({days_left} days ago).")
            elif days_left <= 7:
                warnings.append(f"Item '{item.name}' expires in {days_left} days.")
        if not item.name or len(item.name.strip()) < 2:
            errors.append(f"Item '{item.name}' has an invalid name.")
        if item.quantity is None:
            errors.append(f"Item '{item.name}' is missing a quantity.")
    if not pantry.shopping_lists:
        warnings.append("No shopping lists have been created yet.")
    if not pantry.usage_logs:
        warnings.append("No usage logs have been recorded yet.")
    return {"warnings": warnings, "errors": errors}
