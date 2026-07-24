# === Stage 25: Add daily summary calculations ===
# Project: PantryMate
def generate_daily_summary(items):
    """Generate a compact daily summary for all pantry items."""
    today = datetime.date.today()
    total_items = len(items)
    expired = [i for i in items if i['expiry_date'] and i['expiry_date'] < today]
    days_left = {i['name']: (i['expiry_date'] - today).days if i['expiry_date'] else None for i in items}
    low_stock = [i for i in items if i.get('quantity', 0) <= 3]
    summary = {
        'total_items': total_items,
        'expired_today': len(expired),
        'items_expiring_soon': {name: days for name, days in days_left.items() if days and 7 >= days > 0},
        'low_stock_items': low_stock,
    }
    return summary

if __name__ == '__main__':
    sample_items = [
        {'name': 'Milk', 'expiry_date': datetime.date(2025, 12, 1), 'quantity': 2},
        {'name': 'Bread', 'expiry_date': datetime.date(2026, 3, 15), 'quantity': 4},
        {'name': 'Eggs', 'expiry_date': None, 'quantity': 1},
    ]
    print(generate_daily_summary(sample_items))
