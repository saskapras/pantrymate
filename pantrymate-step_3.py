# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: PantryMate
def validate_required(value, field_name):
    if value is None or (isinstance(value, str) and value.strip() == ''):
        raise ValueError(f"Field '{field_name}' must not be empty")
    return value


def validate_positive_int(value, field_name):
    if not isinstance(value, int) or value <= 0:
        raise ValueError(f"Field '{field_name}' must be a positive integer")
    return value


def validate_short_text(value, max_length=50, min_length=1, field_name=""):
    try:
        text = str(value).strip()
    except Exception:
        raise TypeError(f"Field '{field_name}' must be convertible to string")
    if len(text) < min_length or len(text) > max_length:
        raise ValueError(
            f"Field '{field_name}' must be between {min_length} and {max_length} characters"
        )
    return text


def validate_date_string(value, field_name):
    try:
        datetime.strptime(str(value), "%Y-%m-%d")
    except (ValueError, TypeError):
        raise ValueError(f"Field '{field_name}' must be a date in YYYY-MM-DD format")
    return str(value)
