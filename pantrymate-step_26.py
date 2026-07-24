# === Stage 26: Add weekly summary calculations ===
# Project: PantryMate
def weekly_summary(items):
    """Calculate a compact weekly summary for the pantry."""
    today = datetime.date.today()
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(days=6)

    items_used = [i for i in items if i['usage']['date'] and week_start <= i['usage']['date'] <= week_end]
    items_expiring = [i for i in items if i['expiry_date'] and i['expiry_date'] <= today]

    summary = {
        'week': f'Week of {week_start.strftime("%Y-%m-%d")}',
        'items_used': len(items_used),
        'usage_details': [(u['item_name'], u['quantity']) for u in items_used],
        'expired_items': [e['name'] for e in items_expiring],
    }

    return summary
