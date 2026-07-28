# === Stage 38: Add data integrity checks for broken references ===
# Project: PantryMate
def _get_item(item_id):
    item = items.get(item_id)
    if item is None:
        raise ValueError(f"Item {item_id} not found")
    return item

def _get_shopping_list(list_id):
    sl = shopping_lists.get(list_id)
    if sl is None:
        raise ValueError(f"Shopping list {list_id} not found")
    return sl

def _get_usage_log(log_id):
    ul = usage_logs.get(log_id)
    if ul is None:
        raise ValueError(f"Usage log {log_id} not found")
    return ul

def add_item_to_shopping_list(list_id, item_id, quantity=1):
    sl = _get_shopping_list(list_id)
    item = _get_item(item_id)
    existing = next((e for e in sl["items"] if e["item_id"] == item_id), None)
    if existing:
        existing["quantity"] += quantity
    else:
        sl["items"].append({"item_id": item_id, "quantity": quantity})

def add_usage(item_id, quantity):
    _get_item(item_id)
    now = datetime.now()
    usage_logs[item_id] = usage_logs.get(item_id, []) + [
        {"datetime": now.isoformat(), "quantity": quantity}
    ]

def mark_shopping_list_complete(list_id):
    sl = _get_shopping_list(list_id)
    if not all(i["completed"] for i in sl["items"]):
        raise ValueError("Not all items are marked complete")
    sl["completed"] = True
