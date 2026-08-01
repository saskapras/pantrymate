# === Stage 51: Add unit tests for search and filter behavior ===
# Project: PantryMate
import unittest
from pantrymate.models import PantryItem, PantryListEntry, UsageLog
from datetime import date


class TestSearchAndFilter(unittest.TestCase):
    def setUp(self):
        self.items = [
            PantryItem(name="Olive Oil", expiry_date=date(2030, 6, 1), category="Oil"),
            PantryItem(name="Rice", expiry_date=date(2028, 12, 15), category="Grain"),
            PantryItem(name="Peanut Butter", expiry_date=date(2027, 3, 10), category="Spread"),
        ]
        self.entries = [
            PantryListEntry(item_name="Rice", quantity=2.5, unit="kg"),
            PantryListEntry(item_name="Olive Oil", quantity=1.0, unit="L"),
        ]

    def test_search_by_prefix(self):
        results = PantryItem.search_prefix("oli")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Olive Oil")

    def test_filter_by_category(self):
        filtered = PantryItem.filter_by_category("Oil")
        self.assertEqual(filtered.count(), 1)
        self.assertTrue(filtered[0].is_expired is False)

    def test_list_search_prefix(self):
        results = PantryListEntry.search_prefix("rice")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].item_name, "Rice")

    def test_entry_filter_by_quantity(self):
        filtered = PantryListEntry.filter_by_quantity(min_qty=2.5)
        self.assertEqual(filtered.count(), 1)


if __name__ == "__main__":
    unittest.main()
