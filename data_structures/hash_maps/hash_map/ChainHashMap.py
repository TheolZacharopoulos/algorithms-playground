from data_structures.hash_maps import HashMapBase
from data_structures.hash_maps import UnsortedTableMap


class ChainHashMap(HashMapBase):
    """Hash map implemented with separate chaining for collision resolution."""

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key error: ' + repr(k))
        return bucket[k]

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            # bucket is new to the table
            self._table[j] = UnsortedTableMap()

        old_size = len(self._table[j])
        self._table[j][k] = v

        # increase overall map size
        if len(self._table[j]) > old_size:
            self._n += 1

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key error: ' + repr(k))
        del bucket[k]

    def __iter__(self):
        for bucket in self._table:
            # a nonempty slot
            if bucket is not None:
                for key in bucket:
                    yield key
