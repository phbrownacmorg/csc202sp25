from Stack import Stack

class Queue[T]:
    """Class to represent a queue of objects of type T, 
    implemented as two stacks, an inbox and an outbox.
    The top of the outbox is the head of the queue, and
    the top of the inbox is the tail of the queue."""

    def __init__(self) -> None:
        """Construct an empty queue."""
        self._inbox: Stack[T] = Stack[T]()
        self._outbox: Stack[T] = Stack[T]()

    # Private helper routine

    def _refillOutbox(self) -> None:
        # Pre:
        assert self._outbox.isEmpty() and not self._inbox.isEmpty(), "Refilling at wrong time"
        while not self._inbox.isEmpty():
            self._outbox.push(self._inbox.pop())
        # Post:
        assert self._inbox.isEmpty() and not self._outbox.isEmpty(), "Refill failed"

    # Query methods

    def isEmpty(self) -> bool:
        """Return True iff the queue is empty."""
        return self._inbox.isEmpty() and self._outbox.isEmpty()
    
    def peek(self) -> T:
        """Return the item at the head of the queue."""
        # Pre:
        assert not self.isEmpty(), "Cannot peek an empty queue"
        if self._outbox.isEmpty():
            # Refill the outbox
            self._refillOutbox()
        return self._outbox.peek()
    
    # Mutator methods

    def add(self, new_item: T) -> None:
        """Add NEW_ITEM at the end of the queue."""
        self._inbox.push(new_item)

    def pop(self) -> T:
        """Pop an item off the head of the queue and return it."""
        # Pre:
        assert not self.isEmpty(), "Cannot pop an empty queue"
        if self._outbox.isEmpty():
            # Refill the outbox
            self._refillOutbox()
        return self._outbox.pop()
