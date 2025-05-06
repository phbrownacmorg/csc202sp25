
class MaxHeap[T]:
    """Maxheap of a data type T.  Each item is stored as a tuple (priority, data),
        in which priority is an integer and data is the data value."""
    
    def _invariant(self) -> bool:
        """Class invariant."""
        valid = True
        size: int = len(self._items)
        for i in (range(1, size)): # Don't worry about the root
            # Each item must be less than its parent
            valid = valid and self._items[i] < self._items[(i-1)//2]
        return valid

    def __init__(self) -> None:
        """Construct an empty heap."""
        self._items: list[tuple[int, T]] = []
        # Post:
        assert self._invariant(), "Bad construction"

    # Query methods

    def empty(self) -> bool:
        """Return True iff the heap is empty."""
        return len(self._items) == 0
    
    def __len__(self) -> int:
        """Return the number of items in the heap."""
        return len(self._items)
    
    def peek(self) -> tuple[int, T]:
        """Return the top (maximum) item from the heap, without removing it."""
        # Pre:
        assert len(self) > 0, "Can't peek an empty heap"
        return self._items[0]

    # Mutator methods

    def insert(self, priority: int, value: T) -> None:
        """Insert VALUE into the heap with priority PRIORITY."""
        # Put it at the end
        self._items.append((priority, value))
        # As long as it's bigger than it's parent, swap it upwards
        idx: int = len(self._items) - 1

        # As long as the item is (1) not the root and (2) out of order...
        while idx > 0 and self._items[idx] > self._items[(idx-1)//2]:
            # Swap the item with its parent
            self._items[idx], self._items[(idx-1)//2] = \
                self._items[(idx-1)//2], self._items[idx]
            # Set IDX to the new index of the item we just inserted
            idx = (idx-1)//2
        # Post:
        assert self._invariant()
        # and the heap should be one bigger than it was

    def pop(self) -> T:
        """Returns the data value from the top of the heap,
            removing it from the heap."""
        # Pre:
        assert len(self) > 0, "Can't pop an empty heap"
        result: T = self._items[0][1] # Data value from the top item
        # Remove the last item
        last_item: tuple[int, T] = self._items.pop()
        idx = 0
        out_of_order = (idx < len(self._items)) # True if the root has a child
        while out_of_order:
            # Put the last item in at idx
            self._items[idx] = last_item
            # Percolate that item downwards, if need be

            max_child_idx = 2*idx + 1 # Guess that the left child is bigger
            # If the right child exists and is bigger than the left child, use it
            if (max_child_idx < (len(self._items) - 1)) \
                and (self._items[max_child_idx] < self._items[max_child_idx + 1]):
                max_child_idx += 1

            # Now that we know which child is larger, is it out of order?
            # If it exists and is out of order, then...
            if (max_child_idx < len(self._items)) \
                and (last_item < self._items[max_child_idx]):
                # If so, swap the child up. (Swapping the parent down happens on line 69.)
                # last_item = self._items[idx] # Already true from line 69
                self._items[idx] = self._items[max_child_idx]
                idx = max_child_idx
            else:
                out_of_order = False

        # Post:
        assert self._invariant()
        return result
            
