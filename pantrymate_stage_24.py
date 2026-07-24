# === Stage 24: Add grouped summaries by category or status ===
# Project: PantryMate
def summarize(items, group_by='category'):
    """Return a dict of grouped summaries for pantry items."""
    groups = {}
    for item in items:
        key = item.get(group_by) or 'uncategorized'
        if key not in groups:
            groups[key] = {'count': 0, 'expiry_dates': [], 'status_counts': {}}
        groups[key]['count'] += 1
        expiry = item.get('expiry_date', '')
        days_left = _days_until(expiry) if expiry else None
        if days_left is not None:
            groups[key]['expiry_dates'].append(days_left)
        status = item.get('status', 'active')
        groups[key]['status_counts'][status] = groups[key]['status_counts'].get(status, 0) + 1
    return groups

def _days_until(expiry):
    """Compute days left until expiry from an ISO date string or None."""
    if not expiry:
        return None
    try:
        exp = datetime.fromisoformat(expiry.replace('Z', '+00:00'))
        now = datetime.now(exp.tzinfo) if exp.tzinfo else datetime.utcnow()
        return (exp - now).days
    except Exception:
        return None

def show_summary(groups):
    """Pretty-print grouped summaries."""
    for category, info in groups.items():
        print(f"\n[{category}]")
        print(f"  Total items : {info['count']}")
        if info.get('expiry_dates'):
            avg = sum(info['expiry_dates']) / len(info['expiry_dates'])
            print(f"  Avg days left: {avg:.1f}")
        for status, cnt in info.get('status_counts', {}).items():
            print(f"  Status '{status}': {cnt}")
