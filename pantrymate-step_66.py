# === Stage 66: Add export of a short status dashboard ===
# Project: PantryMate
def dashboard(items, logs, alerts):
    """Compact status dashboard for PantryMate."""
    lines = ["=== PantryMate Dashboard ===", f"Items: {len(items)}", f"Recent logs: {len(logs)}", f"Alerts: {len(alerts)}"]
    if items:
        lines.append(f"First item: {items[0].name}")
    if logs:
        lines.append(f"Last log: {logs[-1].timestamp}")
    if alerts:
        lines.append(f"Lowest stock: {alerts[0].item.name if alerts else 'None'}")
    print("\n".join(lines))
