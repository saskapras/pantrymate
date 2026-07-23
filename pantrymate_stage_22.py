# === Stage 22: Add favorite records and quick favorite listing ===
# Project: PantryMate
class Favorite:
    def __init__(self, item_id=None):
        self.item_id = item_id
    def to_dict(self):
        return {"item_id": self.item_id}
    @classmethod
    def from_dict(cls, d):
        return cls(item_id=d.get("item_id"))

class FavoriteManager:
    def __init__(self):
        self._favorites = []
    def add_favorite(self, item_id):
        if not any(f.item_id == item_id for f in self._favorites):
            self._favorites.append(Favorite(item_id=item_id))
        return len(self._favorites)
    def remove_favorite(self, item_id):
        before = len(self._favorites)
        self._favorites = [f for f in self._favorites if f.item_id != item_id]
        return before - len(self._favorites)
    def list_favorites(self):
        return [f.item_id for f in sorted(self._favorites, key=lambda x: x.item_id)]
    def is_favorite(self, item_id):
        return any(f.item_id == item_id for f in self._favorites)
    def load(self, data):
        if isinstance(data, dict):
            items = data.get("items", [])
            self._favorites = [Favorite(item_id=it["item_id"]) for it in items]
