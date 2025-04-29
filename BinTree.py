from collections.abc import Container
from typing import cast, Iterator

class BinTree[T](Container[T]):
    """Class to represent a binary tree.  The root node is always represented
        as a node, even if the tree is empty.  Other than that, however, an
        empty tree is represented by None.  This tree cannot store the value
        None."""
    
    def _invariant(self) -> bool:
        """Class invariant."""
        valid: bool = True
        # empty node cannot have children
        if self._data is None:
            valid = self._left is None and self._right is None
        return valid

    def __init__(self, data: T | None = None) -> None:
        """Construct a single-node tree with data DATA."""
        self._data: T | None = data
        self._left: BinTree[T] | None = None
        self._right: BinTree[T] | None = None
        # Post:
        assert self._invariant()

    # QUERY METHODS

    def empty(self) -> bool:
        """Return True iff SELF is the empty tree."""
        return self._data is None
    
    def __contains__(self, value: object) -> bool:
        """Return True iff VALUE is contained in the subtree rooted at SELF."""
        contained: bool = False # Handles base case #1; empty tree contains nothing
        if (not self.empty()):
            # Base case #2: Non-empty tree, data matches this node
            if value == self.data():
                contained = True
            elif self.hasLeftChild() or self.hasRightChild(): # Recursive cases
                if self.hasLeftChild():
                    contained = (value in self.left())
                if not contained and self.hasRightChild():
                    contained = (value in self.right())
        return contained
    
    def hasLeftChild(self) -> bool:
        """Return True iff SELF has a non-empty left child."""
        return self._left is not None
    
    def hasRightChild(self) -> bool:
        """Return True iff SELF has a non-empty right child."""
        return self._right is not None
    
    def left(self) -> 'BinTree[T]':
        """Return self._left, but only if self.hasLeftChild"""
        # Pre:
        assert self.hasLeftChild()
        return cast(BinTree[T], self._left)

    def right(self) -> 'BinTree[T]':
        """Return self._right, but only if self.hasRightChild"""
        # Pre:
        assert self.hasRightChild()
        return cast(BinTree[T], self._right)

    def data(self) -> T:
        """Return the data held in this node.  Requires that there be some."""
        # Pre:
        assert not self.empty()
        return cast(T, self._data)
    
    def __len__(self) -> int:
        """Return the number of data nodes in the tree."""
        nodes: int = 1
        if self.empty(): # Base case #1
            nodes = 0

        if self.hasLeftChild():
            nodes = nodes + len(self.left())

        if self.hasRightChild():
            nodes = nodes + len(self.right())
        return nodes
    
    def height(self) -> int:
        """Return the height of the tree."""
        h: int = 1 # Handles the case of a non-empty tree with no children
        if self.empty():
            h = 0
        elif self.hasLeftChild() and self.hasRightChild():
            h = 1 + max(self.left().height(), self.right().height())
        elif self.hasLeftChild(): # No right child
            h = 1 + self.left().height()
        elif self.hasRightChild(): # No left child
            h = 1 + self.right().height()
        return h
    
    # TRAVERSALS

    def __iter__(self) -> Iterator[T]:
        """Iterate over the tree, using an inorder traversal.  Implemented
            as a generator."""
        if not self.empty():
            if self.hasLeftChild():
                # Iterate over the left subtree
                for item in self.left():
                    yield item
            yield self.data()
            if self.hasRightChild():
                # Iterate over the right subtree
                for item in self.right():
                    yield item

    # MUTATOR METHODS

    def setLeft(self, value: T) -> None:
        """Convenience function to add a leaf node with value VALUE as the
            left child of SELF.  *NOTE*: subclasses (such as BST[T]) may add
            more restrictive preconditions to this method, even though that
            violates strict substitutability."""
        # Pre:
        assert (not self.empty()) and (not self.hasLeftChild())
        self._left = BinTree[T](value)
        # Post:
        assert self._invariant() and self.left()._invariant()        

    def setRight(self, value: T) -> None:
        """Convenience function to add a leaf node with value VALUE as the
            right child of SELF.  *NOTE*: subclasses (such as BST[T]) may add
            more restrictive preconditions to this method, even though that
            violates strict substitutability."""
        # Pre:
        assert (not self.empty()) and (not self.hasRightChild())
        self._right = BinTree[T](value)
        # Post:
        assert self._invariant() and self.right()._invariant()

    def removeLeft(self) -> None:
        """Convenience function to remove SELF's left subtree from the tree.
            Does nothing if SELF has no left subtree."""
        self._left = None
        # Post:
        assert self._invariant()

    def removeRight(self) -> None:
        """Convenience function to remove SELF's right subtree from the tree.
            Does nothing if SELF has no right subtree."""
        self._right = None
        # Post:
        assert self._invariant()
