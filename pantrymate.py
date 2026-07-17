# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: PantryMate
from datetime import date, timedelta

class Item:
    def __init__(self, name, quantity, expiry_date):
        self.name = name
        self.quantity = quantity
        self.expiry_date = expiry_date

    def is_expired(self):
        return self.expiry_date < date.today()

    def restock_alert(self):
        remaining_days = (self.expiry_date - date.today()).days
        return "⚠️ " + self.name + " expires in " + str(remaining_days) + " days!" if remaining_days <= 14 else ""


class PantryMate:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity, expiry_date):
        item = Item(name, quantity, expiry_date)
        self.items.append(item)
        return item

    def get_expired_items(self):
        return [item for item in self.items if item.is_expired()]

    def check_alerts(self):
        alerts = []
        for item in self.items:
            alert = item.restock_alert()
            if alert:
                alerts.append(alert)
        return alerts


# Demo Dataset
demo_data = [
    ("Milk", 2, date.today() + timedelta(days=5)),
    ("Eggs", 12, date.today() + timedelta(days=30)),
    ("Yogurt", 4, date.today() - timedelta(days=2)),  # Expired!
    ("Rice", 5, date.today() + timedelta(days=365)),
]

pantry = PantryMate()
for name, qty, expiry in demo_data:
    pantry.add_item(name, qty, expiry)

print("📦 PantryMate Demo")
print("===================")
expired = pantry.get_expired_items()
if expired:
    print("❌ Expired items:", [item.name for item in expired])
else:
    print("✅ No expired items!")

alerts = pantry.check_alerts()
for alert in alerts:
    print(alert)
