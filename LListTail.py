from LList import LList
from typing import cast

class LListTail[T]:
    """Class to represent a linked list with a tail pointer.
    The list itself is implemented using the LList class already developed.
    The tail pointer is defined to point to the sentinel node."""

    def _invariant(self) -> bool:
        """Class invariant."""
        valid: bool = self._head._invariant()
        # Tail pointer must point to an empty list (the sentinel)
        if not self._tail.empty():
            valid = False
        # If the list is empty (the head is also empty), head and tail point to
        #   the *same* sentinel node
        elif self._head.empty() and self._tail != self._head:
            valid = False
        # Otherwise, the head and tail had better be different (implied, because
        #   we already established that the tail points to an empty list and the
        #   head doesn't point to an empty list)
        return valid

    def __init__(self) -> None:
        """Construct an empty list."""
        self._head = LList[T]()
        self._tail = self._head
        # Post:
        assert self._invariant()

    # Query methods
    def empty(self) -> bool:
        """Return True iff the current list is empty."""
        return self._head.empty()
    
    def __str__(self) -> str:
        """Return a string representation of the list."""
        return str(self._head)
    
    def __len__(self) -> int:
        """Return the number of nodes in the list, not counting the sentinel."""
        return len(self._head)
    
    def index(self, value: T) -> int:
        """Returns the index of the first occurrence of VALUE in the list.
        If VALUE is not in the list, raises ValueError."""
        return self._head.index(value)

    def __contains__(self, value: T) -> bool:
        """Return True iff self contains the value VALUE."""
        return value in self._head
    
        # Mutator methods
    def add(self, value: T) -> None:
        """Add a value to the front of the list."""
        self._head.add(value)
        if not self._tail.empty(): # Added to an empty list
            assert self._tail._next is not None, 'for mypy'
            self._tail = self._tail._next
        # Post:
        assert not self.empty() and self._invariant(), "Add failed"

    def pop(self, idx: int = -1) -> T:
        """Remove and return the value at index IDX (default -1).  If the list
          has no index IDX, raise a ValueError.  This method handles negative
          indices, counting from the end as usual."""
        result: T
        # If we're not deleting the last item, no special handling
        if idx != -1 and idx != (len(self._head) - 1):
            result = self._head.pop(idx)
        # If we *are* deleting the last item, need to reset the tail pointer...
        #    which means we have to keep hold of the node we're changing
        else:
            if idx == -1:
                idx = len(self._head) - 1
            assert idx >= 0, "Cannot pop an empty list"
            # Find the node to be deleted (O(n))
            current: LList[T] = self._head
            while idx > 0:
                assert current._next is not None, 'Reached sentinel with idx > 0'
                current = current._next
                idx = idx - 1
            # Verify we're looking at the last node
            assert current._next == self._tail, 'current is not the last node'
            # Delete the current node by copying in the contents
            #  (both _data and _next) from the sentinel
            result = cast(T, current._data) # Order is important!
            current._data = self._tail._data
            current._next = self._tail._next
            self._tail = current

        # Post:
        # result == value from the deleted node AND the list is one shorter than it was AND
        assert self._invariant()
        return result
        