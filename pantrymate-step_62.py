# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: PantryMate
def score_items(items):
    """Score pantry items by urgency: items nearing expiry rank higher."""
    scores = []
    for item in items:
        if item['expiry_date']:
            days_left = (datetime.date.today() + timedelta(days=item['expiry_date'])) - datetime.date.today()
            score = max(0, days_left)
        else:
            score = 365
        scores.append((score, item))
    scores.sort(key=lambda x: x[0])
    return [item for _, item in scores]
