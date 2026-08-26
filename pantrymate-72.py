# === Stage 72: Add Markdown report export ===
# Project: PantryMate
def export_markdown_report(self):
    lines = ["# PantryMate Report\n", "## Items\n"]
    for item in self.items:
        lines.append(f"- {item.name}: {item.quantity} units, expires {item.expiry_date}")
    lines.append("\n## Shopping List\n")
    for item in self.shopping_list:
        lines.append(f"- {item.name}: {item.quantity} units")
    lines.append("\n## Usage Log\n")
    for entry in self.usage_log:
        lines.append(f"- {entry.item_name}: {entry.quantity} units used on {entry.date}")
    lines.append("\n## Restock Alerts\n")
    for alert in self.restock_alerts:
        lines.append(f"- {alert.item_name}: {alert.quantity} units low")
    return "\n".join(lines)
