# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: PantryMate
class SortableMixin:
    """Add flexible sorting to any list-based entity (items, logs, alerts)."""
    
    _SORTABLE_FIELDS = {}
    
    def __init__(self):
        self._sort_order = 'asc'
    
    def set_sort(self, field, order='asc'):
        if field not in self._SORTABLE_FIELDS:
            raise ValueError(f"Field '{field}' is not sortable. Available: {list(self._SORTABLE_FIELDS.keys())}")
        
        valid_orders = ['asc', 'desc']
        if order not in valid_orders:
            raise ValueError(f"Order must be one of {valid_orders}, got '{order}'")
            
        self._sort_order = order
        return self
    
    def get_sort_key(self, item):
        field = self._SORTABLE_FIELDS.get('default', 'id')
        return getattr(item, field, None)
    
    @classmethod
    def sort(cls, items, default_field='id'):
        """Sort a list of objects by any sortable attribute."""
        if not items:
            return []
            
        try:
            mixin = cls()
            mixin._SORTABLE_FIELDS['default'] = default_field
        except Exception:
            return sorted(items, key=lambda x: getattr(x, default_field, 0))
        
        sort_key = lambda item: (getattr(item, 'id', 0), getattr(item, default_field, 0))
        return sorted(items, key=sort_key)
