class Queue[T]:
    """Class to represent a queue of objects of type T, 
    implemented as a Python list.  The end of the list
    is the tail of the queue."""

    def __init__(self) -> None:
        """Construct an empty queue."""
        self._items: list[T] = []

    # Query methods

    def isEmpty(self) -> bool:
        """Return True iff the queue is empty."""
        return len(self._items) == 0
    
    def peek(self) -> T:
        """Return the item at the head of the queue."""
        # Pre:
        assert len(self._items) > 0, "Cannot peek an empty queue"
        return self._items[0]
    
    # Mutator methods

    def add(self, new_item: T) -> None:
        """Add NEW_ITEM at the end of the queue."""
        self._items.append(new_item)

    def pop(self) -> T:
        """Pop an item off the head of the queue and return it."""
        # Pre:
        assert len(self._items) > 0, "Cannot pop an empty queue"
        return self._items.pop(0)
