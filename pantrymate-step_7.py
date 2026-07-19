# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: PantryMate
def format_item(item):
    status = "OK" if item.get("expiry_date", "") == "" else ("EXPIRED" if is_expired(item["expiry_date"]) else f"expires {item['expiry_date']}")
    return f"{item['name'][:25]:<25} | Qty: {item['quantity']:>3} | Status: {status}"

def format_shopping_list(list_items):
    lines = ["Shopping List:", "-"]
    for i, item in enumerate(list_items, 1):
        if isinstance(item, dict):
            lines.append(f"  {i}. {item['name'][:30]:<30} | Qty: {item.get('quantity', '')}")
        else:
            lines.append(f"  {i}. {item}")
    return "\n".join(lines)

def format_usage_log(log_entries):
    lines = ["Usage Log:", "-"]
    for entry in log_entries[-10:]:
        if isinstance(entry, dict):
            date_str = entry.get("date", "unknown")
            items_used = ", ".join([f"{u['name']}: {u['quantity']}x" for u in entry.get("items_used", [])])
            lines.append(f"  [{date_str}] Used: {items_used}")
        else:
            lines.append(str(entry))
    return "\n".join(lines)

def print_pantry_report(pantry):
    print("=" * 70)
    print("  PANTRY REPORT")
    print("=" * 70)
    if pantry["items"]:
        for item in pantry["items"]:
            print(format_item(item))
    else:
        print("  No items in pantry.")
    print("-" * 70)
    shopping = [i for i in pantry["shopping_list"] if isinstance(i, dict)]
    print(format_shopping_list(shopping))
    print("-" * 70)
    log_entries = [e for e in pantry["usage_log"] if isinstance(e, dict)]
    print(format_usage_log(log_entries))

def format_alerts(alerts):
    lines = ["Alerts:", "-"]
    for a in alerts:
        if isinstance(a, dict):
            msg = f"  - {a['message']}"
            if "priority" in a and a["priority"]:
                msg += f" [PRIORITY]"
            lines.append(msg)
        else:
            lines.append(str(a))
    return "\n".join(lines)

def format_restock_suggestions(suggestions):
    lines = ["Restock Suggestions:", "-"]
    for item in suggestions:
        if isinstance(item, dict):
            lines.append(f"  - {item['name']}: add to shopping list")
        else:
            lines.append(str(item))
    return "\n".join(lines)
