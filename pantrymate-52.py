# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: PantryMate
def format_expiry(expiry_str):
    """Return a human-readable expiry date string, or 'Never' if absent."""
    if not expiry_str:
        return "Never"
    try:
        dt = datetime.strptime(expiry_str, "%Y-%m-%d")
        delta = (dt - today).days
        if delta <= 30:
            remaining = f"{delta} days left"
        elif delta < 180:
            months = delta // 30
            remaining = f"{months} months left"
        else:
            years = delta // 365
            remaining = f"{years} year{'s' if years > 1 else ''} left"
        return remaining
    except (ValueError, TypeError):
        return expiry_str


def parse_quantity(raw):
    """Parse a raw quantity string into an integer or None."""
    if not raw:
        return None
    try:
        return int(raw.strip())
    except ValueError:
        return None


def generate_id():
    """Generate a short unique identifier for pantry entries."""
    import random, string
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choices(chars, k=6))


def calculate_shelf_life(days):
    """Convert shelf life in days to a formatted duration string."""
    if days is None:
        return "None"
    years, remainder = divmod(days, 365)
    months, remainder = divmod(remainder, 30)
    parts = []
    if years:
        parts.append(f"{years}y")
    if months:
        parts.append(f"{months}m")
    if days:
        parts.append(f"{days}d")
    return ''.join(parts) or "None"


def validate_date(date_str, fmt="%Y-%m-%d"):
    """Validate a date string and return the parsed datetime object."""
    try:
        return datetime.strptime(date_str, fmt)
    except (ValueError, TypeError):
        raise ValueError(f"Invalid date format '{date_str}', expected {fmt}")


def summarize_shopping_list(items):
    """Summarize a shopping list with grouped quantities and totals."""
    if not items:
        return "Shopping list is empty."
    summary = {}
    for item in items:
        qty = parse_quantity(item.get('quantity', '1')) or 1
        name = item.get('name', 'Unknown')
        summary[name] = summary.get(name, 0) + qty
    total_items = len(items)
    total_qty = sum(summary.values())
    return f"Total items: {total_items}, Total quantity: {total_qty}"
