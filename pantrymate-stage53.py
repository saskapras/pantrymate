# === Stage 53: Add command help text and usage examples ===
# Project: PantryMate
HELP_TEXT = """PantryMate — Kitchen Pantry Manager

Usage:
  pantrymate add <item> [count] [--category <cat>] [--expiry <date>]
  pantrymate remove <item> [count]
  pantrymate list [--category <cat>] [--low-stock] [--expired] [--all]
  pantrymate restock --item <item> [--count <n>] [--category <cat>] [--expiry <date>]
  pantrymate history [--days <n>] [--limit <n>]
  pantrymate alerts [--threshold <n>]

Options:
  --category     Item category (e.g., dairy, grains, canned).
  --expiry       Expiry date as YYYY-MM-DD.
  --count        Quantity to add/remove (default 1).
  --all          Show all items regardless of expiry or stock level.
  --low-stock    Show only items with stock below threshold.
  --expired      Show only expired items.
  --days         Filter history entries older than N days.
  --limit        Maximum number of results to display (default 20).
  --threshold    Restock alert threshold; default is 5 units.

Examples:
  pantrymate add "Milk" 4 --category dairy --expiry 2026-12-31
  pantrymate add "Rice" 2kg --category grains
  pantrymate remove "Eggs" 2
  pantrymate list --category dairy --low-stock
  pantrymate restock --item Milk --count 4 --expiry 2027-06-01
  pantrymate history --days 30 --limit 5
  pantrymate alerts --threshold 3

For more help, run: pantrymate --help"""
