# === Stage 34: Add support for multiple local user profiles ===
# Project: PantryMate
import json
from pathlib import Path

PROFILE_DIR = Path.home() / ".pantrymate" / "profiles"


def load_profiles():
    profiles = {}
    for p in PROFILE_DIR.glob("*.json"):
        with open(p) as f:
            data = json.load(f)
        if isinstance(data, dict):
            name = data.get("name", p.stem)
            user_id = data.get("user_id") or data.get("id")
            profiles[user_id] = {"name": name, "data": data}
    return profiles


def save_profile(user_id, profile_data):
    PROFILE_DIR.mkdir(parents=True, exist_ok=True)
    path = PROFILE_DIR / f"{user_id}.json"
    with open(path, "w") as f:
        json.dump(profile_data, f, indent=2)
