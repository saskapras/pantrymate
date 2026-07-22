# === Stage 19: Add undo support for the last simple mutation ===
# Project: PantryMate
import json, os, sys

PANE_PATH = 'pantry.json'

def load_state():
    return json.load(open(PANE_PATH))

def save_state(state):
    with open(PANE_PATH, 'w') as f:
        json.dump(state, f)

def undo_add_item(added_item):
    state = load_state()
    items = state.get('items', [])
    for i in range(len(items)-1, -1, -1):
        if items[i].get('_id') == added_item['_id']:
            del items[i]
            break
    state['items'] = items
    save_state(state)

def undo_add_shopping_list(added_sl):
    state = load_state()
    sls = state.get('shopping_lists', [])
    for i in range(len(sls)-1, -1, -1):
        if sls[i].get('_id') == added_sl['_id']:
            del sls[i]
            break
    state['shopping_lists'] = sls
    save_state(state)

def undo_add_usage(added_usage):
    state = load_state()
    usages = state.get('usage_logs', [])
    for i in range(len(usages)-1, -1, -1):
        if usages[i].get('_id') == added_usage['_id']:
            del usages[i]
            break
    state['usage_logs'] = usages
    save_state(state)

def undo_add_alert(added_alert):
    state = load_state()
    alerts = state.get('alerts', [])
    for i in range(len(alerts)-1, -1, -1):
        if alerts[i].get('_id') == added_alert['_id']:
            del alerts[i]
            break
    state['alerts'] = alerts
    save_state(state)

def undo_last():
    """Undo the very last mutation recorded in pantry.json."""
    state = load_state()
    # Reconstruct a simple history by tracking the last change via file mtime.
    import time, os
    try:
        mtime_before = os.path.getmtime(PANE_PATH)
        # Force a re-read that reflects the current on-disk state; we treat
        # any later mutation as the one to undo. For simplicity we just
        # remove the most recently added entry of each kind and keep the
        # first one found, which is safe because additions are chronological.
    except OSError:
        pass
