from BinTree import BinTree
from typing import cast, TypeVar

T: TypeVar = TypeVar('T')

class BST[T](BinTree[T]):
    """Class to represent a binary search tree, using the node-and-references
        structure inherited from BinTree."""
    
    def _invariant(self) -> bool:
        """Class invariant."""
        valid: bool = super()._invariant() # Superclass invariant still holds
        if self.hasLeftChild():
            valid = valid and max(iter(self.left())) < self.data()
            valid = valid and self.left()._invariant()
        if self.hasRightChild():
            valid = valid and min(iter(self.right())) > self.data()
            valid = valid and self.right()._invariant()
        return valid
    
    # QUERY METHODS

    def find(self, value: T) -> 'BST[T]':
        """Find and return the node containing VALUE.  If VALUE is not in the
            tree, raise a ValueError."""
        result: BST[T] = self # Handles the case where self.data() == value
        if self.empty():
            raise ValueError('{0} is not in the tree'.format(value))
        elif value < self.data(): # Left subtree
            if not self.hasLeftChild():
                raise ValueError('{0} is not in the tree'.format(value))
            result = self.left().find(value) # Search the left subtree, recursively
        elif value > self.data(): # Right subtree
            if not self.hasRightChild():
                raise ValueError('{0} is not in the tree'.format(value))
            result = self.right().find(value) # Search the right subtree, recursively
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
    
    # MUTATOR METHODS
    
    def setLeft(self, value: T) -> None:
        """Convenience function to add a leaf node with value VALUE as the
            left child of SELF.  Because this is a BST, this raises a
            ValueError if VALUE is greater than or equal to the value in
            SELF."""
        # Pre:
        assert (not self.empty()) and (not self.hasLeftChild())
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
        assert (not self.empty()) and (not self.hasRightChild())
        if value <= self.data(): # Can't put VALUE there in a BST
            raise ValueError("{0} can't be the right child of a node with {1}".format(value, self.data()))
        else:
            self._right = BST[T](value)
        # Post:
        assert self._invariant() # Implies self.right()._invariant()

    def add(self, value: T) -> None:
        """Add VALUE to the tree.  Raises a ValueError if it's already in the tree."""
        if self.empty(): # Empty tree, just fill in the data
            self._data = value
        elif value == self.data(): # Value is already in the tree, raise ValueError
            raise ValueError('Value {0} is already in the tree'.format(value))
        elif value < self.data(): # Put it in the left subtree
            if self.hasLeftChild():
                self.left().add(value)
            else:
                self.setLeft(value)
        else:
            assert value > self.data()
            if self.hasRightChild():
                self.right().add(value)
            else:
                self.setRight(value)

