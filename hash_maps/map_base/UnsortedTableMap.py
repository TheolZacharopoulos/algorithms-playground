# Relies on storing key-value pairs in arbitrary order within a Python list.

from hash_maps.map_base.MapBase import MapBase


class UnsortedTableMap(MapBase):
    """Map implementation using an unordered list."""

    def __init__(self):
        self._table = []

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""

        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key error: ' + repr(k))

    def __setitem__(self, key, value):
        """Assign value v to key k, overwriting existing value if present."""

        # Found a match: reassign value and quit
        for item in self._table:
            if key == item._key:
                item._value = value
                return

        # did not find match for key, create a new one
        self._table.append(self._Item(key, value))

    def __delitem__(self, key):
        """Remove item associated with key k (raise KeyError if not found)"""

        # Found a match: remove item and quit
        for i in range(len(self._table)):
            if self._table[i]._key == key:
                self._table.pop(i)
                return
        raise KeyError('Key error: ' + repr(key))

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        """Generate iteration of the map s keys."""
        for item in self._table:
            yield item._key
    