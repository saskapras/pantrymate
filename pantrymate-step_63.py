# === Stage 63: Add relationships between records where useful ===
# Project: PantryMate
class PantryMate:
    def __init__(self):
        self.items = {}
        self.shopping_lists = {}
        self.usage_logs = {}
        self.restock_alerts = {}
        self.item_shopping = {}
        self.item_usage = {}
        self.item_alert = {}
        self.item_shopping_list = {}

    def add_item(self, name, expiry_date, quantity, unit):
        item_id = f"{name}_{expiry_date}"
        self.items[item_id] = {"name": name, "expiry_date": expiry_date, "quantity": quantity, "unit": unit}
        self.item_shopping[item_id] = []
        self.item_usage[item_id] = []
        self.item_alert[item_id] = False
        self.item_shopping_list[item_id] = []
        return item_id

    def add_to_shopping_list(self, item_id, quantity):
        if item_id not in self.item_shopping_list:
            self.item_shopping_list[item_id] = []
        self.item_shopping_list[item_id].append(quantity)

    def log_usage(self, item_id, quantity):
        if item_id not in self.item_usage:
            self.item_usage[item_id] = []
        self.item_usage[item_id].append(quantity)

    def set_alert(self, item_id, alert):
        self.item_alert[item_id] = alert
