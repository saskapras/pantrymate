# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: PantryMate
def generate_changelog(activity_log, max_entries=50):
    entries = activity_log[-max_entries:]
    lines = ["=== PantryMate Changelog ===", ""]
    for i, entry in enumerate(entries, 1):
        lines.append(f"{i}. {entry}")
    lines.append("")
    lines.append("Generated from activity log.")
    return "\n".join(lines)
