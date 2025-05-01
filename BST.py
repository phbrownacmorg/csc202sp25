from BinTree import BinTree
from typing import cast, TypeVar

class BST[T](BinTree[T]):
    """Class to represent a binary search tree, using the node-and-references
        structure inherited from BinTree.  There is no empty BST, only None."""
    
    def _invariant(self) -> bool:
        """Class invariant."""
        # Pre:
        assert hasattr(self._data, '__lt__') and hasattr(self._data, '__gt__')
        valid: bool = super()._invariant() # Superclass invariant still holds
        if self.hasLeftChild():
            valid = valid and isinstance(self._left, BST) # Just BinTree doesn't cut it
            valid = valid and self._data > max(iter(self._left)) # type: ignore
            valid = valid and self.left()._invariant()
        if self.hasRightChild():
            valid = valid and isinstance(self._right, BST) # Just BinTree doesn't cut it
            valid = valid and self._data < min(iter(self._right)) # type: ignore
            valid = valid and self.right()._invariant()
        return valid
    
    # QUERY METHODS

    def smallestValue(self) -> T:
        """Find and return the smallest value in the subtree rooted at SELF."""
        return cast(T, 1) # Bogosity incarnate

    def largestValue(self) -> T:
        """Find and return the largest value in the subtree rooted at SELF."""
        return cast(T, 1) # Bogosity incarnate

    def find(self, value: T) -> 'BST[T]':
        """Find and return the node containing VALUE.  If VALUE is not in the
            tree, raise a ValueError."""
        # Pre: some assertions about T
        assert hasattr(value, '__lt__') and hasattr(value, '__gt__')
        result: BST[T] = self # Handles the case where self.data() == value
        # Left subtree
        if value < self.data(): 
            if not self.hasLeftChild():
                raise ValueError('{0} is not in the tree'.format(value))
            result = cast(BST[T], self.left()).find(value) # Search the left subtree, recursively
        elif value > self.data(): # Right subtree
            if not self.hasRightChild():
                raise ValueError('{0} is not in the tree'.format(value))
            result = cast(BST[T], self.right()).find(value) # Search the right subtree, recursively
        return result

    def __contains__(self, value: object) -> bool:
        """Return True iff VALUE is contained in the subtree rooted at SELF."""
        present: bool = False
        try:
            self.find(cast(T, value))
            present = True # We didn't get an error, so VALUE is in the tree
        except ValueError:
            pass # present is already False
        return present
    
    def successorValueRChild(self) -> T:
        """Returns the successor value for a node with a right child in a BST."""
        # Pre:
        assert self.hasRightChild()
        return cast(BST[T], self.right()).largestValue()
    
    def generalSuccessorValue(self) -> T | None:
        """Returns the successor value for SELF in the tree, or None if SELF
            is the largest node in the tree."""
        # Pre:
        assert hasattr(self, 'parent') # Can't be done without parent links
        result: T | None = None
        return result  # Stub!

    # MUTATOR METHODS
    
    def setLeft(self, value: T) -> None:
        """Convenience function to add a leaf node with value VALUE as the
            left child of SELF.  Because this is a BST, this raises a
            ValueError if VALUE is greater than or equal to the value in
            SELF."""
        # Pre:
        assert (not self.hasLeftChild()) and hasattr(value, '__ge__')
        if value >= self.data(): # Can't put VALUE there in a BST
            raise ValueError("{0} can't be the left child of a node with {1}".format(value, self.data()))
        else:
            self._left = BST[T](value)
        # Post:
        assert self._invariant() # Implies self.left()._invariant()

    def setRight(self, value: T) -> None:
        """Convenience function to add a leaf node with value VALUE as the
            left child of SELF.  Because this is a BST, this raises a
            ValueError if VALUE is less than or equal to the value in
            SELF."""
        # Pre:
        assert (not self.hasRightChild()) and hasattr(value, '__le__')
        if value <= self.data(): # Can't put VALUE there in a BST
            raise ValueError("{0} can't be the right child of a node with {1}".format(value, self.data()))
        else:
            self._right = BST[T](value)
        # Post:
        assert self._invariant() # Implies self.right()._invariant()

    def add(self, value: T) -> None:
        """Add VALUE to the tree.  Raises a ValueError if it's already in the tree."""
        # Pre:
        assert hasattr(value, '__lt__') and hasattr(value, '__gt__')
        if value == self.data(): # Value is already in the tree, raise ValueError
            raise ValueError('Value {0} is already in the tree'.format(value))
        elif value < self.data(): # Put it in the left subtree
            if self.hasLeftChild():
                cast(BST[T], self.left()).add(value)
            else:
                self.setLeft(value)
        else:
            assert value > self.data()
            if self.hasRightChild():
                cast(BST[T], self.right()).add(value)
            else:
                self.setRight(value)

    def remove(self, value: T) -> 'BST[T]':
        """Remove the node containing VALUE from the tree, and return the
            resulting tree.  If VALUE is not in the tree, raise a ValueError."""
        return BST[T](cast(T, 'bogus'))

