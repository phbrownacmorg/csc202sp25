from typing import cast

class Queue[T]:
    """Class to represent a queue of objects of type T, 
    implemented as a circular queue using a Python list.
    This implementation cannot store the value None."""

    def _invariant(self) -> bool:
        """Class invariant."""
        return 0 <= self._head < self._slots \
                and 0 <= self._tail < self._slots \
                and self._items[self._tail] is None # tail points to an empty slot
                # Implies self._slots > 0

    def __init__(self) -> None:
        """Construct an empty queue."""
        INITIAL_SLOTS: int = 4
        self._slots = INITIAL_SLOTS
        self._items: list[T | None] = [None] * INITIAL_SLOTS
        self._head = 0
        self._tail = 0

    # Query methods

    def isEmpty(self) -> bool:
        """Return True iff the queue is empty."""
        return self._items[self._head] is None # Head is an empty slot
        
    def peek(self) -> T:
        """Return the item at the head of the queue."""
        # Pre:
        assert not self.isEmpty(), "Cannot peek an empty queue"
        return cast(T, self._items[self._head])
    
    # Mutator methods

    def add(self, new_item: T) -> None:
        """Add NEW_ITEM at the end of the queue."""
        # Pre:
        assert self._items[self._tail] is None, "Queue overflow"
        self._items[self._tail] = new_item
        self._tail = (self._tail + 1) % self._slots
        if self._items[self._tail] is not None: # Full queue
            # Resize
            newQ: list[T | None] = [None] * (2 * self._slots) # Double the size
            newTail: int = 0
            while self._items[self._head] is not None: # Transfer the contents
                newQ[newTail] = self._items[self._head]
                self._items[self._head] = None
                self._head = (self._head + 1) % self._slots
                newTail = newTail + 1
            self._items = newQ
            self._head = 0
            self._tail = newTail
            self._slots = self._slots * 2
        # Post:
        assert self._invariant(), "Adding failed"

    def pop(self) -> T:
        """Pop an item off the head of the queue and return it."""
        # Pre:
        assert not self.isEmpty(), "Cannot pop an empty queue"
        value: T = cast(T, self._items[self._head])
        self._items[self._head] = None
        self._head = (self._head + 1) % self._slots
        return value
