# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: PantryMate
def filter_items(items, status=None, category=None, owner=None, tag=None):
    results = items.copy()
    if status is not None:
        results = [i for i in results if getattr(i, 'status', '') == status]
    if category is not None:
        results = [i for i in results if getattr(i, 'category', '').lower() == category.lower()]
    if owner is not None:
        results = [i for i in results if getattr(i, 'owner', '').lower() == owner.lower()]
    if tag is not None:
        results = [i for i in results if tag in (getattr(i, 'tags', []) or [])]
    return results
