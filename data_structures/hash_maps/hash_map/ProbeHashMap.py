from data_structures.hash_maps import HashMapBase

class ProbeHashMap(HashMapBase):
    """Hash map implemented with linear probing for collision resolution."""

    # sentinel marks locations of previous deletions
    _AVAIL = object()

    def _is_available(self, j):
        return self._table[j] is None or self._table[j] == ProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        """Search for key k in bucket at index j.

        Return (success, index) tuple, described as follows:
        If match was found, success is True and index denotes its location.
        If no match found, success is False and index denotes first available slot."""

        first_avail = None

        while True:
            if self._is_available(j):
                if first_avail is None:
                    # mark this as first avail
                    first_avail = j

                if self._table[j] is None:
                    # search has failed
                    return False, first_avail

                elif k == self._table[j]._key:
                    # found a match
                    return True, j

                # keep looking (cyclically)
                j = (j + 1) % len(self._table)

    def _bucket_getitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))
        return self._table[s].value

    def _bucket_setitem(self, j, k, v):
        found, s = self._find_slot(j, k)

        if not found:
            # insert new item
            self._table[s] = self._Item(k, v)
            self._n += 1
        else:
            # overwrite existing
            self._table[s]._value = v

    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))

        # mark as vacated
        self._table[s] = ProbeHashMap._AVAIL

    def __iter__(self):
        for j in range(len(self._table)):
            if not self._is_available(j):
                yield self._table[j].key

