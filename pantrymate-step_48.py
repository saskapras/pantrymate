# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: PantryMate
import unittest
from pantrymate.models import PantryItem, Shelf
from datetime import date


class TestPantryItem(unittest.TestCase):
    def test_create_item(self):
        item = PantryItem(name="Milk", quantity=2, unit="L", expiry=date(2026, 12, 31))
        self.assertEqual(item.name, "Milk")
        self.assertTrue(item.is_expired(), f"Expected expired, got {item.expiry}")

    def test_create_fresh_item(self):
        item = PantryItem(name="Rice", quantity=5, unit="kg", expiry=date(2030, 1, 1))
        self.assertFalse(item.is_expired())

    def test_invalid_expiry_date_raises(self):
        with self.assertRaises(ValueError):
            PantryItem(name="Bad", expiry=date.today())


class TestShelf(unittest.TestCase):
    def test_add_item_to_shelf(self):
        shelf = Shelf()
        item = PantryItem(name="Olive Oil", quantity=1, unit="L")
        shelf.add(item)
        self.assertEqual(len(shelf), 1)

    def test_remove_item_from_shelf(self):
        shelf = Shelf()
        item = PantryItem(name="Salt", quantity=3, unit="kg")
        shelf.add(item)
        shelf.remove(item)
        self.assertEqual(len(shelf), 0)


if __name__ == "__main__":
    unittest.main()
