# === Stage 36: Add templates for quickly creating common records ===
# Project: PantryMate
def create_template_item(name, category="general", quantity=1):
    return {"name": name, "category": category, "quantity": quantity}

def create_template_shopping_list():
    return []

def get_quick_add_prompt(item_name=None, expiry_days=None):
    if item_name:
        return f"Add '{item_name}' to pantry."
    prompt = "What would you like to add?"
    if expiry_days is not None:
        prompt += f"\nSuggested expiry: {expiry_days} days from now."
    return prompt

def quick_create_item(name, category="general", quantity=1):
    item = create_template_item(name, category, quantity)
    print(f"Created item: {item}")
    return item

def quick_add_to_shopping_list():
    list_ = create_template_shopping_list()
    print("Shopping list initialized.")
    return list_
