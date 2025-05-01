from collections.abc import Collection
from typing import cast, Iterator
from Q2Stacks import Queue

class BinTree[T](Collection[T]):
    """Class to represent a binary tree.  There are no empty nodes; an empty
        tree is just represented by None."""
    
    def _invariant(self) -> bool:
        """Class invariant."""
        valid: bool = True
        # Verify consistency of parent and child nodes
        if self._parent is not None:
            valid = ((self._parent._left == self) or (self._parent._right == self))
        if valid and self._left is not None:
            valid = (self._left._parent == self)
        if valid and self._right is not None:
            valid = (self._right._parent == self)
        return valid

    def __init__(self, data: T) -> None:
        """Construct a single-node tree with data DATA."""
        self._data: T = data
        self._parent: BinTree[T] | None = None
        self._left: BinTree[T] | None = None
        self._right: BinTree[T] | None = None
        # Post:
        assert self._invariant()

    # QUERY METHODS

    def data(self) -> T:
        """Return the data held in this node."""
        return self._data

    def isRoot(self) -> bool:
        """Return True iff SELF is the root (that is, has no parent)."""
        return self._parent is None
    
    def hasLeftChild(self) -> bool:
        """Return True iff SELF has a non-empty left child."""
        return self._left is not None
    
    def hasRightChild(self) -> bool:
        """Return True iff SELF has a non-empty right child."""
        return self._right is not None
    
    def parent(self) -> 'BinTree[T]':
        """Return SELF's parent, but only if SELF is not the root."""
        # Pre:
        assert not self.isRoot()
        return self._parent

    def left(self) -> 'BinTree[T]':
        """Return self._left, but only if self.hasLeftChild()"""
        # Pre:
        assert self.hasLeftChild()
        return cast(BinTree[T], self._left)

    def right(self) -> 'BinTree[T]':
        """Return self._right, but only if self.hasRightChild()"""
        # Pre:
        assert self.hasRightChild()
        return cast(BinTree[T], self._right)

    def __contains__(self, value: object) -> bool:
        """Return True iff VALUE is contained in the subtree rooted at SELF."""
        contained: bool = False
        # Base case #2: Non-empty tree, data matches this node
        if value == self.data():
            contained = True
        elif self.hasLeftChild() or self.hasRightChild(): # Recursive cases
            if self.hasLeftChild():
                contained = (value in self.left())
            if not contained and self.hasRightChild():
                contained = (value in self.right())
        return contained
    
    def __len__(self) -> int:
        """Return the number of data nodes in the tree."""
        nodes: int = 1 # Current node
        if self.hasLeftChild():
            nodes = nodes + len(self.left())
        if self.hasRightChild():
            nodes = nodes + len(self.right())
        return nodes
    
    def height(self) -> int:
        """Return the height of the tree."""
        h: int = 1 # Height of the current node
        if self.hasLeftChild() and self.hasRightChild():
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
        if self.hasLeftChild():
            # Iterate over the left subtree
            for item in self.left():
                yield item
        yield self.data()
        if self.hasRightChild():
            # Iterate over the right subtree
            for item in self.right():
                yield item

    def preorder(self) -> Iterator[T]:
        """Iterate over the tree, using a depth-first preorder traversal.
            Implemented as a generator."""
        yield self.data()
        if self.hasLeftChild():
            # Iterate over the left subtree
            for item in self.left().preorder():
                yield item
        if self.hasRightChild():
            # Iterate over the right subtree
            for item in self.right().preorder():
                yield item

    def bf_preorder(self) -> Iterator[T]:
        """Iterate over the tree, using a breadth-first preorder traversal.
            Implemented as a generator."""
        q: Queue[BinTree[T]] = Queue[BinTree[T]]()
        q.add(self)
        while not q.isEmpty():
            current: BinTree[T] = q.pop()
            yield current.data()
            if current.hasLeftChild():
                q.add(current.left())
            if current.hasRightChild():
                q.add(current.right())

    # MUTATOR METHODS

    def setLeft(self, value: T) -> None:
        """Convenience function to add a leaf node with value VALUE as the
            left child of SELF.  *NOTE*: subclasses (such as BST[T]) may add
            more restrictive preconditions to this method, even though that
            violates strict substitutability."""
        # Pre:
        assert not self.hasLeftChild()
        self._left = BinTree[T](value)
        self._left._parent = self
        # Post:
        assert self._invariant() and self.left()._invariant()        

    def setRight(self, value: T) -> None:
        """Convenience function to add a leaf node with value VALUE as the
            right child of SELF.  *NOTE*: subclasses (such as BST[T]) may add
            more restrictive preconditions to this method, even though that
            violates strict substitutability."""
        # Pre:
        assert not self.hasRightChild()
        self._right = BinTree[T](value)
        self._right._parent = self
        # Post:
        assert self._invariant() and self.right()._invariant()

    def removeLeft(self) -> None:
        """Convenience function to remove SELF's left subtree from the tree.
            Does nothing if SELF has no left subtree."""
        if self.hasLeftChild():
            self._left._parent = None
        self._left = None
        # Post:
        assert self._invariant()

    def removeRight(self) -> None:
        """Convenience function to remove SELF's right subtree from the tree.
            Does nothing if SELF has no right subtree."""
        if self.hasRightChild():
            self._right._parent = None
        self._right = None
        # Post:
        assert self._invariant()
