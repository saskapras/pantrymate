# === Stage 27: Add monthly summary calculations ===
# Project: PantryMate
def monthly_summary(data):
    """Compute a compact monthly summary from pantry data."""
    items = data.get("items", [])
    logs = data.get("logs", [])
    alerts = data.get("alerts", [])
    months = {}
    for log in logs:
        m = log["month"]
        if m not in months:
            months[m] = {"used": [], "added": 0, "expired": 0}
        months[m]["used"].append(log)
        for item in items:
            if item.get("expiry_month") == m and item.get("status") == "expired":
                months[m]["expired"] += 1
    for alert in alerts:
        m = alert["month"]
        if m not in months:
            months[m] = {"used": [], "added": 0, "expired": 0}
        months[m]["alerts"].append(alert)
    return dict(sorted(months.items()))
