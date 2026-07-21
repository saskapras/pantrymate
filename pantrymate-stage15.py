# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: PantryMate
def dispatch(text_command):
    text = text_command.strip().lower()
    if not text:
        return {"status": "error", "message": "Empty command"}
    
    # Command routing table
    commands = {
        "help": lambda cmd, context: {"status": "ok", "message": "Commands: add, list, search, check, restock, usage"},
        "add": lambda cmd, context: {"status": "pending", "message": "Add item to pantry. Use 'add <name> <expiry>'"},
        "list": lambda cmd, context: {"status": "pending", "message": "List all items in the pantry"},
        "search": lambda cmd, context: {"status": "pending", "message": "Search pantry by keyword. Use 'search <keyword>'"},
        "check": lambda cmd, context: {"status": "pending", "message": "Check expiry status of all items"},
        "restock": lambda cmd, context: {"status": "pending", "message": "View restock suggestions for low-stock items"},
        "usage": lambda cmd, context: {"status": "pending", "message": "Log item usage. Use 'usage <item_name> <quantity>'"}
    }
    
    # Find matching command
    for key in commands:
        if text.startswith(key):
            return commands[key](text_command, None)
    
    return {"status": "error", "message": f"Unknown command: '{text_command}'"}
