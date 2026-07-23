# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: PantryMate
import json, os

def archive_records(db_path="pantrymate.db"):
    """Move completed/expired records to an archive JSON file."""
    if not os.path.exists(db_path):
        return
    arch_path = db_path + ".archive"
    with open(db_path) as f:
        records = json.load(f)
    active, archived = [], []
    for r in records:
        status = r.get("status", "active")
        if status == "completed" or (r.get("expiry_date") and r["expiry_date"] < "2030-01-01"):
            archived.append(r)
        else:
            active.append(r)
    with open(db_path, "w") as f:
        json.dump(active, f, indent=2)
    if archived:
        with open(arch_path, "a") as af:
            json.dump(archived, af, indent=2)

def restore_records(db_path="pantrymate.db"):
    """Move all records back to the active database."""
    arch_path = db_path + ".archive"
    if not os.path.exists(arch_path):
        return 0
    with open(arch_path) as f:
        archived = json.load(f)
    with open(db_path) as f:
        active = json.load(f)
    merged = active + archived
    with open(db_path, "w") as f:
        json.dump(merged, f, indent=2)
    os.remove(arch_path)
    return len(archived)
