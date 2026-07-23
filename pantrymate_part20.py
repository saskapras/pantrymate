# === Stage 20: Add duplicate detection for newly created records ===
# Project: PantryMate
import hashlib

def detect_duplicates(items, new_item):
    """Check if a new pantry item already exists in the list."""
    for i in items:
        # Compare name and quantity to find duplicates
        if i['name'].lower() == new_item['name'].lower():
            return True
    return False

def add_duplicate_check_to_pantry(pantry):
    """Add duplicate detection function to pantry module."""
    pantry['detect_duplicates'] = detect_duplicates

# Example usage:
if __name__ == '__main__':
    test_items = [
        {'name': 'Rice', 'quantity': 5},
        {'name': 'Pasta', 'quantity': 3}
    ]
    
    new_item = {'name': 'rice', 'quantity': 2}
    
    if detect_duplicates(test_items, new_item):
        print("Duplicate detected!")
    else:
        print("Item is unique")
