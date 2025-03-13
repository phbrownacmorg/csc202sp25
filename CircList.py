from LList import LList

class CircList[T]:
    """Class to represent a circular linked list.  The nodes are instances of
    LList[T] with no sentinel, linked in a loop."""

    def _invariant(self) -> bool:
        valid = False
        if self._tail is None: # Empty list
            valid = True
        else:
            current: LList[T] = self._tail
            while (current._next is not None) and (current._next is not self._tail):
                current = current._next
            if current._next is self._tail: # Circle complete
                valid = True
            # If current._next is None, then valid should be False, but it already is
        return valid

    def __init__(self) -> None:
        """Construct an empty list."""
        self._tail: LList[T] | None = None

    def empty(self) -> bool:
        """Return True iff the current list is empty."""
        return self._tail is None
    
    def __str__(self) -> str:
        """Return a string representation of the list."""
        result: str = "∅"
        if not self.empty():
            current: LList[T] = self._tail._next
            result = '❬' + str(current._data) + '❭➞'
            while current._next is not self._tail._next:
                current = current._next
                result = result + '❬' + str(current._data) + '❭➞'
            result = result + "∅"
        return result
    
    def __len__(self) -> int:
        """Return the number of nodes in the list."""
        result: int = 0 # Correct if list is empty
        if not self.empty():
            result = 1
            current: LList[T] = self._tail._next
            while current != self._tail:
                result += 1
                current = current._next
        return result
    
    def index(self, value: T) -> int:
        """Returns the index of the first occurrence of VALUE in the list.
        If VALUE is not in the list, raises ValueError."""
        if self.empty():
            raise ValueError('Value "{0}" is not in empty list'.format(value))
        else:
            idx: int = 0
            current: LList[T] = self._tail._next
            while current._data != value and current is not self._tail:
                current = current._next
                idx += 1
            if current._data != value: # value wasn't in the list
                raise ValueError('Value "{0}" is not in the list'.format(value))
            return idx
        
    def __contains__(self, value: T) -> bool:
        """Return True iff self contains the value VALUE."""
        contains = True
        try:
            self.index(value)
        except ValueError:
            contains = False
        return contains

    # Mutator methods
    def add(self, value: T) -> None:
        """Add a value to the front of the list."""
        newNode: LList[T] = LList[T]()
        newNode._data = value
        if self._tail is None:
            newNode._next = newNode
            self._tail = newNode
        else:
            newNode._next = self._tail._next
            self._tail._next = newNode
        # Post:
        assert self._invariant() and newNode._data == value and self._tail._next is newNode

    def pop(self, idx: int = -1) -> T:
        """Remove and return the value at index IDX (default -1).  If the list
           has no index IDX, raise a ValueError.  This method handles negative
           indices, counting from the end as usual."""
        # Pre: -(length of list) <= idx < length of list
        assert not self.empty(), "Can't pop from an empty list."
        # Handle negative indices (still checking precondition)
        length: int = len(self)
        if idx < 0:
            idx = idx + length
            if idx < 0:
                raise ValueError("IDX < -(length of list)")
        elif idx >= length:
            raise ValueError('IDX >= length of list')
        
        value: T
        # Special case for one node
        if length == 1:
            assert idx == 0, "Miscount"
            value = self._tail._data
            self._tail = None
        # More than one node
        else:
            prev: LList[T] = self._tail # Node *before* the one to delete
            while idx > 0:
                prev = prev._next
                idx -= 1
            victim: LList[T] = prev._next
            value = victim._data
            prev._next = victim._next
            if self._tail is victim:
                self._tail = prev
        return value

        

