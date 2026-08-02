# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: PantryMate
def colorize(text, color):
    codes = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'cyan': '\033[96m',
        'bold': '\033[1m',
    }
    reset = '\033[0m'
    if color in codes:
        return f"{codes[color]}{text}{reset}"
    return text

def print_report(items, alerts):
    print(colorize("=== PantryMate Report ===", "bold"))
    for i in items:
        status = colorize("EXPIRED", 'red') if i['expiry'] < today() else (colorize("OK", 'green'))
        print(f"  {i['name']:15s} | Qty: {i['quantity']} | Expires: {i['expiry'].strftime('%Y-%m-%d')} | Status: {status}")
    if alerts:
        print(colorize("--- Restock Alerts ---", "yellow"))
        for a in alerts:
            print(f"  Buy more of: {a['item_name']} (current stock: {a['quantity']})")
