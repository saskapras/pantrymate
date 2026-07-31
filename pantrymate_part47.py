# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: PantryMate
def demo():
    pantry = Pantry()

    # Step 1: Add items to the pantry with expiry dates
    pantry.add_item("Milk", "2025-04-15")
    pantry.add_item("Eggs (dozen)", "2025-03-20")
    pantry.add_item("Rice (5kg)", "2026-01-01")

    # Step 2: Generate a shopping list for items expiring soon
    alerts = pantry.get_expiry_alerts(days=90)
    print(f"Items expiring soon: {alerts}")

    # Step 3: Create a usage log entry
    today = "2025-01-15"
    pantry.log_usage("Milk", today, amount=0.5)
    print(f"Milk remaining after usage: {pantry.get_remaining('Milk')}")

    # Step 4: Create a shopping list for items with low stock
    shopping_list = pantry.create_shopping_list(threshold=2)
    print(f"Shopping list: {shopping_list}")

    # Step 5: Check if any item is about to expire and needs restocking
    needs_restock, soon_to_expire_items = pantry.needs_restock(days=30)
    print(f"Needs restock: {needs_restock}, Items: {soon_to_expire_items}")

    # Step 6: Display the full pantry status
    print("\n=== Pantry Status ===")
    for item, info in pantry.get_all_items().items():
        print(f"{item}: Stock={info['quantity']} units, Expires on {info['expiry_date']}")


demo()
