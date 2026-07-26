# === Stage 32: Add pagination helpers for long console output ===
# Project: PantryMate
def paginate(text, page_size=40):
    """Split a long string into pages of ~page_size lines."""
    if not text:
        return []
    lines = text.splitlines()
    pages = [lines[i:i+page_size] for i in range(0, len(lines), page_size)]
    result = ["--- Page {}/{} ---".format(p+1, len(pages)) for p in range(len(pages))]
    for page in pages:
        result.append("\n".join(page))
    return "\n\n".join(result)

def pretty_table(headers, rows):
    """Format a list of records into aligned columns."""
    if not headers or not rows:
        return ""
    widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, val in enumerate(row):
            widths[i] = max(widths[i], len(str(val)))
    sep = " | ".join("-" * w for w in widths)
    out = ["  " + sep]
    out.append("  " + " | ".join(str(h).ljust(w) for h, w in zip(headers, widths)))
    for row in rows:
        out.append("  " + " | ".join(str(v).ljust(w) for v, w in zip(row, widths)))
    return "\n".join(out)

def format_expiry(date_str):
    """Format a date string with human-readable label."""
    if not date_str:
        return "Unknown"
    try:
        from datetime import datetime, timedelta
        dt = datetime.strptime(date_str[:10], "%Y-%m-%d")
        today = datetime.now()
        diff = (dt - today).days
        label = ""
        if diff < 0:
            label = f"EXPIRED {abs(diff)} days ago!"
        elif diff <= 3:
            label = "Expires in {} days".format(diff)
        else:
            label = "Good for {} more days".format(diff)
        return date_str + " | " + label
    except Exception:
        return date_str
