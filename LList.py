from typing import cast

class LList[T]:
    """Class to represent a linked list.  It depends on the definition that a
    linked list is either:
       1.  An empty list, or
       2.  A node followed by a linked list.
    As such, this implementation uses a sentinel node to represent the empty
    list at the end, so it's possible to call list methods on an empty list."""
    
    def _invariant(self) -> bool:
        """Class invariant."""
        # Either this is an empty list (= sentinel node),
        valid: bool = self._data is None and self._next is None
        # or it's a node with a list after it
        if not valid: # non-empty
            valid = (self._data is not None and self._next is not None) \
                    and self._next._invariant()
        return valid

    def __init__(self) -> None:
        """Create an empty list."""
        self._data: T | None = None
        self._next: LList[T] | None = None
        # Post:
        assert self._invariant()

    # Query methods
    def empty(self) -> bool:
        """Return True iff the current list is empty."""
        return self._data is None and self._next is None
    
    def data(self) -> T:
        return self._data
    
    def rest(self) -> 'LList[T]':
        return self._next

    def __str__(self) -> str:
        """Return a string representation of the list."""
        result: str = "∅"
        if not self.empty():
            result = '❬' + str(self._data) + '❭➞' + str(self._next)
        return result

    def __len__(self) -> int:
        """Return the number of nodes in the list, not counting the sentinel."""
        count: int = 0 # Correct for empty list
        if not self.empty():
            count = 1 + len(cast(LList[T], self._next))
        return count
    
    def index(self, value: T) -> int:
        """Returns the index of the first occurrence of VALUE in the list.
        If VALUE is not in the list, raises ValueError."""
        result: int = -1
        if self.empty(): # If the list is empty, raise a ValueError
            raise ValueError('Value "{0}" is not in empty list'.format(value))
        elif self._data == value: # If this is the node we're looking for, return 0
            result = 0
        else: # VALUE might be farther along, but it isn't in this node
            result = 1 + self._next.index(value)
        # Post:
        assert result >= 0
        return result


    def __contains__(self, value: T) -> bool:
        """Return True iff self contains the value VALUE."""
        result: bool = False # Correct for an empty list
        if not self.empty():
            if self._data == value: # If it's in the current node, we're done
                result = True
            else: # If it's not in the current node, it might be in the rest of the list
                result = value in cast(LList[T], self._next)

        return result

    # Mutator methods
    def add(self, value: T) -> None:
        """Add a value to the front of the list."""
        # Order is important!  Make the new node *first*, and *then*
        #   update self.
        newNode: LList[T] = LList[T]()
        newNode._next = self._next
        newNode._data = self._data
        self._next = newNode
        self._data = value
        # Post:
        assert self._data == value and self._invariant()

    def pop(self, idx: int = -1) -> T:
        """Remove and return the value at index IDX (default -1).  If the list
          has no index IDX, raise a ValueError.  This method handles negative
          indices, counting from the end as usual."""
        result: T
        # Handle negative indices
        if idx < 0:
            idx = idx + len(self)
            assert idx >= 0, "IDX < -len(self)"
            result = self.pop(idx)
        elif self.empty():
            raise ValueError("Cannot pop an empty list")
        elif idx == 0: 
            # Delete the current node by copying in the contents
            #  (both _data and _next) from the next node
            result = cast(T, self._data) # Order is important!
            self._data = cast(LList[T], self._next)._data
            self._next = cast(LList[T], self._next)._next
        else: # idx > 0
            result = cast(LList[T], self._next).pop(idx - 1)
        # Post:
        # result == value from the deleted node AND the list is one shorter than it was AND
        assert self._invariant()
        return result
