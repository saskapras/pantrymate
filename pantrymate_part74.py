# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: PantryMate
def compare_pantry_snapshots(before, after):
    """Compare two pantry states and return additions, removals, and expiry changes."""
    before_keys = {item.name.lower(): item for item in before}
    after_keys = {item.name.lower(): item for item in after}

    added = [after_keys[k] for k in after_keys if k not in before_keys]
    removed = [before_keys[k] for k in before_keys if k not in after_keys]
    common = set(before_keys.keys()) & set(after_keys.keys())

    expiry_changes = []
    for k in common:
        old = before_keys[k]
        new = after_keys[k]
        if old.expiry_date != new.expiry_date:
            expiry_changes.append({
                "name": k,
                "old_expiry": old.expiry_date,
                "new_expiry": new.expiry_date,
            })

    return {"added": added, "removed": removed, "expiry_changes": expiry_changes}
