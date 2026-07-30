# === Stage 44: Add backup creation for the data file ===
# Project: PantryMate
import json, os
from datetime import datetime

def create_backup(data_path):
    backup_dir = "backups"
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"{data_path}.bak_{timestamp}"
    try:
        with open(data_path, "r", encoding="utf-8") as src:
            data = json.load(src)
        with open(backup_file, "w", encoding="utf-8") as dst:
            json.dump(data, dst, indent=2)
        print(f"Backup saved to {backup_file}")
    except Exception as e:
        print(f"Backup failed: {e}")
