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
            valid = valid and self._data > cast(BST[T], self._left).largestValue()
            valid = valid and self.left()._invariant()
        if self.hasRightChild():
            valid = valid and isinstance(self._right, BST) # Just BinTree doesn't cut it
            valid = valid and self._data < cast(BST[T], self._right).smallestValue()
            valid = valid and self.right()._invariant()
        return valid
    
    # QUERY METHODS

    def smallestValue(self) -> T:
        """Find and return the smallest value in the subtree rooted at SELF."""
        result: T = self.data() # Handles the case where there is no left subtree
        if self.hasLeftChild():
            result = cast(BST[T], self.left()).smallestValue()
        return result

    def largestValue(self) -> T:
        """Find and return the largest value in the subtree rooted at SELF."""
        result: T = self.data() # Handles the case where there is no right subtree
        if self.hasRightChild():
            result = cast(BST[T], self.right()).largestValue()
        return result

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
        return cast(BST[T], self.right()).smallestValue()
    
    def generalSuccessor(self) -> 'BST[T] | None':
        """Returns the successor node for SELF in the tree, or None if SELF
            is the largest node in the tree."""
        # Pre:
        assert hasattr(self, 'parent') # Can't be done without parent links
        result: BST[T] | None = None
        return result  # Stub!  FIX THIS.

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
            self._left._parent = self
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
            self._right._parent = self
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

    def remove(self, value: T) -> 'BST[T] | None':
        """Remove the node containing VALUE from the tree, and return the
            resulting tree.  If VALUE is not in the tree, raise a ValueError."""
        # Pre:
        assert hasattr(value, '__lt__') and hasattr(value, '__gt__')
        result: BST[T] | None = self
        if value < self.data():
            # Value should be in left subtree
            if not self.hasLeftChild():
                raise ValueError("{0} cannot be deleted, as it isn't in the tree.".format(value))
            self._left = cast(BST[T], self.left()).remove(value)
        elif value > self.data():
            # Value should be in right subtree
            if not self.hasRightChild():
                raise ValueError("{0} cannot be deleted, as it isn't in the tree.".format(value))
            self._right = cast(BST[T], self.right()).remove(value)
        else: # value == self.data(), so this is the node we're looking for
            # Leaf: just delete it
            if not self.hasRightChild() and not self.hasLeftChild():
                self._parent = None
                result = None
            # Only left child: link around self
            elif self.hasLeftChild() and not self.hasRightChild():
                result = cast(BST[T], self.left())
                self.left()._parent = self._parent
                self._parent = None
                self._left = None
            # Only right child: link around self
            elif self.hasRightChild() and not self.hasLeftChild():
                result = cast(BST[T], self.right())
                self.right()._parent = self._parent
                self._parent = None
                self._right = None
            # Two children
            else:
                # Find the successor value and copy it into self
                self._data = self.successorValueRChild()
                # Then remove it from the right subtree 
                # (successor node cannot have a left child)
                self._right = cast(BST[T], self.right()).remove(self.data())
        

        return result

