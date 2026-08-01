# === Stage 50: Add unit tests for import and export behavior ===
# Project: PantryMate
import json, os, tempfile


def test_roundtrip(tmp):
    import pantrymate as pm
    items = [{"name": "milk", "qty": 2, "expiry": "2026-01-15"}, {"name": "flour", "qty": 1.5}]
    logs = [{"item": "eggs", "date": "2025-12-04"}]
    alerts = [{"item": "milk", "days_left": 3}]

    data = {
        "items": items,
        "logs": logs,
        "alerts": alerts,
        "version": pm.__version__,
    }
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "pantry.json")
        pm.export(data, path)
        assert os.path.exists(path), "exported file missing"

        with open(path) as f:
            loaded = json.load(f)

        assert loaded["version"] == data["version"], "version mismatch after import/export"
        assert len(loaded["items"]) == 2 and loaded["items"][0]["name"] == "milk", "item roundtrip failed"
        assert loaded["logs"][0]["date"] == "2025-12-04", "log date not preserved"
        assert any(a["days_left"] == 3 for a in loaded["alerts"]), "alert data lost"

    # verify import error on missing file
    with tempfile.TemporaryDirectory() as d:
        bad = os.path.join(d, "nope.json")
        try:
            pm.import_data(bad)
            assert False, "should have raised ImportError"
        except (ImportError, FileNotFoundError):
            pass  # expected

    print("PantryMate import/export unit tests passed.")
