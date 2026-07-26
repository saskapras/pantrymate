# === Stage 31: Add compact table rendering for long lists ===
# Project: PantryMate
def render_compact_table(headers, rows):
    """Render a compact table suitable for long lists."""
    if not headers:
        return ""
    col_widths = [len(str(h)) for h in headers]
    max_rows = 30
    display_rows = rows[:max_rows]
    lines = ["| " + " | ".join(f"{col} {w}" for col, w in zip(headers, col_widths)) + " |"]
    lines.append("|" + "|".join("-" * (w + 2) for w in col_widths) + "|")
    for row in display_rows:
        vals = [str(v)[:col_widths[i]] if i < len(row) else "" for i in range(len(headers))]
        lines.append("| " + " | ".join(vals) + " |")
    return "\n".join(lines)
