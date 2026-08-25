# === Stage 67: Add a function that returns key project metrics ===
# Project: PantryMate
def get_project_metrics(self):
        """Return key metrics for the PantryMate project."""
        metrics = {
            "total_items": len(self.items),
            "items_expiring_soon": sum(1 for i in self.items if i.expiry_date and i.expiry_date < self.today),
            "items_expiring_later": sum(1 for i in self.items if i.expiry_date and i.expiry_date >= self.today),
            "total_shopping_list": len(self.shopping_list),
            "usage_log_entries": len(self.usage_log),
            "restock_alerts_triggered": len(self.restock_alerts),
            "unique_categories": len(set(i.category for i in self.items if i.category)),
            "last_updated": self.today.isoformat(),
        }
        return metrics
