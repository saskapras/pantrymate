# === Stage 40: Add plain text report export ===
# Project: PantryMate
def export_text_report(self):
    """Export pantry status to a plain text report."""
    lines = []
    lines.append("=== PantryMate Report ===")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")
    
    lines.append("--- Items ---")
    for item in self.items:
        exp = f"{item.expiry_date.strftime('%Y-%m-%d')}" if item.expiry_date else "No expiry"
        if item.quantity <= 0:
            status = "[EXHAUSTED]"
        elif item.is_used and not item.restocked:
            status = "[USED]"
        else:
            status = ""
        lines.append(f"{item.name}: {item.quantity} units, expires {exp}{status}")
    
    if not self.items:
        lines.append("  (empty)")
    
    lines.append("")
    lines.append("--- Expiring Soon (<30 days) ---")
    expiring = [i for i in self.items if item.expiry_date and item.expiry_date - datetime.now() < timedelta(days=30)]
    if expiring:
        for item in expiring:
            days_left = (item.expiry_date - datetime.now()).days
            lines.append(f"  {item.name}: {days_left} days left")
    else:
        lines.append("  None!")
    
    lines.append("")
    lines.append("--- Low Stock (<5 units) ---")
    low_stock = [i for i in self.items if item.quantity > 0 and item.quantity < 5]
    if low_stock:
        for item in low_stock:
            lines.append(f"  {item.name}: {item.quantity} units")
    else:
        lines.append("  All stocked!")
    
    return "\n".join(lines)
