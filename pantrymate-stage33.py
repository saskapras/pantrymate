# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: PantryMate
DEFAULT_SETTINGS = {
    "low_stock_threshold": 5,
    "expiry_warning_days": 14,
    "auto_refresh_interval_seconds": 300,
    "notification_sound": True,
    "theme": "light",
}


def get_settings():
    return DEFAULT_SETTINGS.copy()


def update_settings(updates: dict) -> dict:
    settings = get_settings()
    for key, value in updates.items():
        if key not in DEFAULT_SETTINGS:
            raise KeyError(f"Unknown setting key: {key}")
        settings[key] = value
    return settings
