# === Stage 4: Implement create operations for the primary records ===
# Project: PantryMate
class PantryItem:
    def __init__(self, name, quantity=1, expiry_date=None):
        self.name = name
        self.quantity = quantity
        self.expiry_date = expiry_date

    def to_dict(self):
        return {
            "name": self.name,
            "quantity": self.quantity,
            "expiry_date": self.expiry_date.isoformat() if self.expiry_date else None
        }


class ShoppingList:
    def __init__(self, name="Default List"):
        self.name = name
        self.items = []

    def add_item(self, item_name, quantity=1):
        self.items.append({"item": item_name, "quantity": quantity})

    def to_dict(self):
        return {
            "name": self.name,
            "items": self.items
        }


class UsageLog:
    def __init__(self, item_name, quantity_used, date=None):
        self.item_name = item_name
        self.quantity_used = quantity_used
        self.date = date

    def to_dict(self):
        return {
            "item_name": self.item_name,
            "quantity_used": self.quantity_used,
            "date": self.date.isoformat() if self.date else None
        }


class RestockAlert:
    def __init__(self, item_name, threshold_quantity=1):
        self.item_name = item_name
        self.threshold_quantity = threshold_quantity

    def to_dict(self):
        return {
            "item_name": self.item_name,
            "threshold_quantity": self.threshold_quantity
        }
