# === Stage 42: Add CSV export without external dependencies ===
# Project: PantryMate
import csv, os

class PantryMateCSV:
    def export_items(self, items_path="pantry_items.csv"):
        with open(items_path, "w", newline="") as f:
            w = csv.writer(f)
            for it in self.items.values():
                w.writerow([it.name, str(it.quantity), it.unit,
                             it.expiry_date if it.expiry_date else "",
                             it.category])

    def export_shopping(self, shopping_path="pantry_shopping.csv"):
        with open(shopping_path, "w", newline="") as f:
            w = csv.writer(f)
            for sl in self.shopping_lists.values():
                w.writerow([sl.name, ", ".join(sl.items)])

    def export_usage(self, usage_path="pantry_usage.csv"):
        with open(usage_path, "w", newline="") as f:
            w = csv.writer(f)
            for u in self.usage_logs:
                w.writerow([u.item_name, str(u.quantity_used), u.date])

    def export_alerts(self, alerts_path="pantry_alerts.csv"):
        with open(alerts_path, "w", newline="") as f:
            w = csv.writer(f)
            for a in self.alerts:
                w.writerow([a.item_name, str(a.days_left), a.expiry_date])

    def export_all(self):
        if not os.path.exists("pantry_items.csv"):
            return "No data to export"
        self.export_items()
        self.export_shopping()
        self.export_usage()
        self.export_alerts()
        print("All pantry reports exported.")
