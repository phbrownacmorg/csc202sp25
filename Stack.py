class Stack[T]:
    """Class to represent a stack of objects of type T, 
    implemented as a Python list.  The end of the list
    is the top of the stack."""

    def __init__(self) -> None:
        """Construct an empty stack."""
        self._items: list[T] = []

    # Query methods

    def isEmpty(self) -> bool:
        """Return True iff the stack is empty."""
        return len(self._items) == 0
    
    def peek(self) -> T:
        # Pre:
        assert len(self._items) > 0, "Cannot peek an empty stack"
        return self._items[-1]
    
    # Mutator methods

    def push(self, new_item: T) -> None:
        """Push NEW_ITEM on top of the stack."""
        self._items.append(new_item)

    def pop(self) -> T:
        """Pop an item off the stack and return it."""
        # Pre:
        assert len(self._items) > 0, "Cannot pop an empty stack"
        return self._items.pop()
