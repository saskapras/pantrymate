# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: PantryMate
import unittest
from pantrymate.core import PantryItem, PantryList, PantryManager


class TestUpdateEdgeCases(unittest.TestCase):
    def setUp(self):
        self.manager = PantryManager()
        self.item1 = PantryItem("Olive Oil", "2026-03-15")
        self.item2 = PantryItem("Pasta", "2027-01-01")
        self.list1 = PantryList("Groceries")

    def test_update_item_preserves_other_fields(self):
        self.manager.add_item(self.item1)
        self.item1.name = "Olive Oil (Extra Virgin)"
        self.item1.update()
        self.assertEqual(self.item1.name, "Olive Oil (Extra Virgin)")
        self.assertEqual(self.item1.expiry_date, "2026-03-15")

    def test_update_item_invalid_date_raises(self):
        self.manager.add_item(self.item1)
        with self.assertRaises(ValueError):
            self.item1.expiry_date = "not-a-date"
            self.item1.update()

    def test_delete_nonexistent_item_returns_false(self):
        result = self.manager.delete_item("Nonexistent")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
