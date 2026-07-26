# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: PantryMate
def parse_date_from_user(prompt):
    """Ask the user for a date in any common format and return it as an ISO string."""
    while True:
        raw = input(prompt).strip()
        if not raw:
            print("Error: Date cannot be empty. Please try again.")
            continue
        formats = [
            "%Y-%m-%d", "%m/%d/%Y", "%d-%m-%Y",
            "%Y/%m/%d", "%m-%d-%Y", "%d/%m/%Y",
            "%d %B %Y", "%d %b %Y"
        ]
        for fmt in formats:
            try:
                return datetime.strptime(raw, fmt).strftime("%Y-%m-%d")
            except ValueError:
                continue
        print("Error: Unrecognized date format. Try YYYY-MM-DD or MM/DD/YYYY.")
