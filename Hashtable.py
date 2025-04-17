import collections.abc as abc
from typing import ClassVar
from LList import LList

class Hashtable[KT, VT](abc.MutableMapping[KT, VT]):
    """Class to represent a hash table, using a very simple hash function.
        Hash chaining is used to handle collisions."""
    
    INITIAL_SIZE: ClassVar[int] = 4

    @classmethod
    def hashval(cls, key: KT) -> int:
        """Calculate a very basic letter-hash value."""
        value: int = 0
        if not isinstance(key, str):
            value = key.__hash__()
        else: # key is a string.  Figure the hash value.
            key = key.upper() # Ignore case
            for c in key:
                value = value + (ord(c) - ord('A') + 1)
            value = abs(value)
        return value

    def __init__(self) -> None:
        """Construct an empty hash table."""
        self._size = Hashtable.INITIAL_SIZE
        self._table: list[LList[tuple[KT, VT]]] = [LList[tuple[KT, VT]]()] * self._size

    # Private helper method
    def _resize(self) -> None:
        """Double the size of the table.  Call this when lambda gets too high."""

    def _bin_idx(self, key: KT, bin_num: int) -> int:
        """Return the index of KEY in the hash chain self._table[bin_num], or -1 if
            KEY is not in that hash chain."""
        result: int = -1
        current: LList[KT, VT] = self._table[bin_num]
        current_idx: int = 0
        while result == -1 and not current.empty():
            if current.data()[0] == key:
                result = current_idx
            current = current.rest()
            current_idx += 1
        return current_idx

    # QUERY METHODS

    def tablesize(self) -> int:
        """Return the current number of bins in the table."""
        return self._size

    def size(self) -> int:
        """Return the number of (key, value) pairs in the hashtable."""
        return len(self)
    
    def __len__(self) -> int:
        """Return the number of (key, value) pairs in the hashtable."""
        return 0 # Stub! Replace with real code.

    def get(self, key: KT) -> VT | None:
        """Takes a KEY and returns the associated value, or None if KEY is not
            in the hashtable."""
        value: VT | None
        try:
            value = self[key]
        except KeyError:
            value = None
        return value
    
    def __getitem__(self, key: KT) -> VT:
        """Takes a KEY and returns the associated value.  If KEY is not in the
           hashtable, raise KeyError."""
        bin_num: int = Hashtable.hashval(key) % self.tablesize()
        bin_idx: int = self._bin_idx(key, bin_num)
        if bin_idx == -1: # KEY is not present
            raise KeyError
        bin: LList[KT, VT] = self._table[bin_num]
        while bin_idx > 0:
            bin = bin.rest()
            bin_idx = bin_idx - 1
            # Invariant: 
            assert not bin.empty() and bin_idx >= 0
        return bin.data()[1]
        
    def __contains__(self, key: KT) -> bool:
        """Returns True if KEY is in the hashtable, or False if not."""
        contained: bool = False
        try:
            self[key]
            contained = True
        except KeyError:
            pass
        return contained
    
    def __iter__(self) -> None:
        """Returns an iterator over the keys in the hashtable."""
        raise NotImplementedError

    # MUTATOR METHODS

    def put(self, key: KT, value: VT) -> None:
        """Put a (KEY, VALUE) pair into the hash table.  If KEY already has
            an associated value, replace it with VALUE."""
        self[key] = value # Delegate to __setitem__
        
    def __setitem__(self, key: KT, value: VT) -> None:
        """Put a (KEY, VALUE) pair into the hash table.  If KEY already has
            an associated value, replace it with VALUE."""
        bin_num: int = Hashtable.hashval(key) % self.tablesize()
        bin_idx: int = self._bin_idx(key, bin_num)
        if bin_idx >= 0: # If KEY is present, remove it
            self._table[bin_num].pop(bin_idx)
        # Now, we know KEY is not present, so we can just add (KEY, VALUE)
        self._table[bin_num].add((key, value))

    def __delitem__(self, key: KT) -> None:
        """Takes a KEY and removes the associated (key, value) pair from the
            hashtable."""
        
