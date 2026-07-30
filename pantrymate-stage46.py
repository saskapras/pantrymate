# === Stage 46: Add a schema version field and migration helper ===
# Project: PantryMate
SCHEMA_VERSION = 3


def migrate_to_v3(items):
    """Upgrade item records to include a 'last_restocked' field."""
    for item in items:
        if "last_restocked" not in item:
            item["last_restocked"] = item.get("added_date", "2024-01-01")


def get_schema_version():
    return SCHEMA_VERSION
