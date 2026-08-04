# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: PantryMate
def bulk_delete_items(pantry, confirm=False):
    """Delete multiple pantry items at once. Requires explicit confirmation to prevent accidental loss."""
    if not confirm:
        raise ValueError("Bulk delete requires an explicit confirmation flag.")
    
    deleted_count = 0
    
    for item in list(pantry.items.values()):
        # Delete associated usage logs and shopping list entries
        item.usage_logs.clear()
        
        # Check if there are active shopping list items
        has_active_shopping_list_items = any(
            sl_item.item_id == item.id 
            and not sl_item.completed 
            for sl_item in item.shopping_list_items
        )
        
        if has_active_shopping_list_items:
            raise ValueError(f"Cannot delete '{item.name}' while it has active shopping list items.")
        
        # Delete associated restock alerts that are pending or overdue
        pending_overdue_alerts = [
            alert for alert in item.restock_alerts 
            if alert.status == AlertStatus.PENDING or alert.status == AlertStatus.OVERDUE
        ]
        
        if pending_overdue_alerts:
            raise ValueError(f"Cannot delete '{item.name}' while it has {len(pending_overdue_alerts)} active restock alerts.")
        
        # Delete the item itself and its associated shopping list items
        deleted_count += 1
        item.shopping_list_items.clear()
        del pantry.items[item.id]
    
    if deleted_count > 0:
        print(f"Successfully deleted {deleted_count} pantry items.")
    
    return deleted_count
