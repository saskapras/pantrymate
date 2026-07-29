# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: PantryMate
def repair(data):
    """Fix common data integrity issues in pantry records."""
    if isinstance(data, dict) and 'items' in data:
        items = data['items']
        fixed_items = []
        for item in items:
            if not isinstance(item, dict):
                continue
            new_item = {k: v for k, v in item.items() if k != 'id'}
            if 'expiry_date' in new_item and new_item['expiry_date'] == '':
                new_item['expiry_date'] = None
            new_item['quantity'] = int(new_item.get('quantity', 0))
            fixed_items.append(new_item)
        data['items'] = fixed_items
    if isinstance(data, dict) and 'shopping_list' in data:
        shopping_list = data['shopping_list']
        data['shopping_list'] = list(shopping_list)
    return data
