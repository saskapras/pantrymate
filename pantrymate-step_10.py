# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: PantryMate
def search_items(query, items=None):
    if items is None:
        from pantrymate.items import get_all_items
        items = get_all_items()
    query_lower = query.lower().strip()
    searchable_fields = ['name', 'category']
    results = [item for item in items if any(
        q.lower() in str(getattr(item, field)).lower()
        for q, field in zip(query_lower.split(), searchable_fields)
    )]
    return sorted(results, key=lambda i: i.name.lower())
