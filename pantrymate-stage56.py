# === Stage 56: Add compact error classes for domain failures ===
# Project: PantryMate
class PantryMateError(Exception):
    """Base error for all pantry operations."""


class ItemNotFoundError(PantryMateError):
    """Raised when a requested pantry item does not exist."""


class ExpiryExceededError(PantryMateError):
    """Raised when an item's expiry date has passed and is still marked edible."""


class DuplicateItemError(PantryMateError):
    """Raised when adding the same item (name + category) twice to one shelf."""


class InvalidDateError(PantryMateError):
    """Raised when a supplied date is malformed or in the past relative to today."""


class InsufficientStockError(PantryMateError):
    """Raised when requested quantity exceeds what's available on the shelf."""


class ShelfFullError(PantryMateError):
    """Raised when trying to add more items than the shelf capacity allows."""


class ShoppingListEmptyError(PantryMateError):
    """Raised when attempting a checkout with no items selected in the list."""


class UsageLogMissingError(PantryMateError):
    """Raised when an entry is missing required fields like item or quantity."""


class RestockAlertDisabledError(PantryMateError):
    """Raised when a restock alert fires but notifications are turned off."""


class ConflictError(PantryMateError):
    """Generic conflict between concurrent operations (e.g. two users editing same shelf)."""


class ValidationError(PantryMateError):
    """Raised for malformed input such as empty names or out-of-range quantities."""
