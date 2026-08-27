# === Stage 73: Add a lightweight HTML report export ===
# Project: PantryMate
def export_report(pantry):
    """Generate a simple HTML report of the pantry state."""
    html = "<html><head><title>PantryMate Report</title></head><body>"
    html += "<h1>PantryMate Report</h1>"
    html += "<table border='1'><tr><th>Item</th><th>Qty</th><th>Expires</th><th>Restock</th></tr>"
    for item in pantry:
        html += f"<tr><td>{item['name']}</td><td>{item['qty']}</td>"
        html += f"<td>{item['expiry'] or 'N/A'}</td>"
        html += f"<td>{'Yes' if item['restock'] else 'No'}</td></tr>"
    html += "</table></body></html>"
    return html
