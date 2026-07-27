# === Stage 35: Add active user switching and user-specific records ===
# Project: PantryMate
class User:
    def __init__(self, name):
        self.name = name
        self.shopping_list = []
        self.usage_logs = {}  # item -> count used by this user

    def add_to_shopping(self, item_name):
        if item_name not in self.shopping_list:
            self.shopping_list.append(item_name)

    def log_usage(self, item_name, amount=1):
        if item_name not in self.usage_logs:
            self.usage_logs[item_name] = 0
        self.usage_logs[item_name] += amount


# Global active user (switched via set_active_user())
_current_user = None


def set_active_user(user):
    global _current_user
    _current_user = user
