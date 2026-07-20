# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: PantryMate
def safe_load(path):
    """Load pantry data from JSON, returning a dict with friendly errors."""
    try:
        import json as _json
    except ImportError:
        return {"error": "Missing stdlib json module"}
    try:
        with open(path, encoding="utf-8") as f:
            raw = _json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(
            f"PantryMate data file not found at {path}. Use save_data() first."
        )
    except (ValueError, json.JSONDecodeError) as exc:
        return {"error": "Malformed JSON", "detail": str(exc)}
    if isinstance(raw, dict):
        for key in ("items", "shopping_list", "usage_logs"):
            if key not in raw and key != "error":
                raise KeyError(
                    f"JSON missing expected key {key!r}. Expected a pantry structure."
                )
        return raw
    else:
        return {"error": "JSON root must be an object (dict)."}
