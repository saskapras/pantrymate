# === Stage 18: Add an activity log with timestamps and action names ===
# Project: PantryMate
class ActivityLog:
    def __init__(self):
        self.entries = []

    def log(self, action_name, details=None):
        entry = {"timestamp": datetime.now().isoformat(), "action": action_name}
        if details is not None:
            entry["details"] = details
        self.entries.append(entry)

    @property
    def history(self):
        return list(reversed(self.entries))
