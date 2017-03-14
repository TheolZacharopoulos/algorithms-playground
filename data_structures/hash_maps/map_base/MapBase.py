# The MutableMapping abstract base class, from Python’s collections module is a valuable tool when implementing a map.
from abc import abstractmethod
from collections import MutableMapping


class MapBase(MutableMapping):
    """Our own abstract base class that includes a nonpublic Item class."""

    @abstractmethod
    def __getitem__(self, key):
        pass

    @abstractmethod
    def __delitem__(self, key):
        pass

    @abstractmethod
    def __setitem__(self, key, value):
        pass

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __len__(self):
        pass

    class _Item:

        """Lightweight composite to store key-value pairs as map items."""
        """The __slots__ declaration takes a sequence of instance variables and reserves just enough space in each
        instance to hold a value for each variable."""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            # compare items based on their keys
            return self._key == other._key

        def __ne__(self, other):
            return self._key != other._key

        def __lt__(self, other):
            return self._key < other._key

