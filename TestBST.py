import unittest
from typing import cast
from BST import BST
# import the code you want to test here

class TestBST(unittest.TestCase):

    def setUp(self) -> None:
        self._1item = BST[str]('garbage')

        self._L1tree = BST[str]('garbage')                  #        garbage
        self._L1tree.add('five')                            #        /
                                                            #      five

        self._R1tree = BST[str]('five')                     #       five
        self._R1tree.add('garbage')                         #          \
                                                            #           garbage

        self._bothSidesNow = BST[str]('infinity')           #       infinity
        self._bothSidesNow.add('five')                      #        /    \
        self._bothSidesNow.add('garbage')                   #     five    left
        self._bothSidesNow.add('left')                      #        \
                                                            #       garbage                                                         

        self._numTree = BST[int](55)                        #         55
        self._numTree.add(26)                               #        /  \
        self._numTree.add(66)                               #      26    66
        self._numTree.add(13)                               #     /  \     \
        self._numTree.add(38)                               #   13    38    82
        self._numTree.add(82)                               #        /     /  \
        self._numTree.add(28)                               #      28    70    104
        self._numTree.add(70)
        self._numTree.add(104)

    # Every method that starts with the string "test"
    # will be executed as a unit test

    # smallestValue, largestValue

    def testSmallestOne(self) -> None:
        self.assertEqual(self._1item.smallestValue(), 'garbage')

    def testSmallestOnlyLeftChild(self) -> None:
        self.assertEqual(self._L1tree.smallestValue(), 'five')

    def testSmallestOnlyRightChild(self) -> None:
        self.assertEqual(cast(BST[int], self._numTree.right()).smallestValue(), 66)

    def testSmallestTwoChildren(self) -> None:
        self.assertEqual(self._numTree.smallestValue(), 13)

    def testSmallestRightHook(self) -> None:
        self.assertEqual(self._bothSidesNow.smallestValue(), 'five')

    def testSmallestLeftHook(self) -> None:
        self.assertEqual(cast(BST[int], self._numTree.right().right()).smallestValue(), 70)

    def testLargestOne(self) -> None:
        self.assertEqual(self._1item.largestValue(), 'garbage')

    def testLargestOnlyLeftChild(self) -> None:
        self.assertEqual(self._L1tree.largestValue(), 'garbage')

    def testLargestOnlyRightChild(self) -> None:
        self.assertEqual(cast(BST[int], self._numTree.right()).largestValue(), 104)

    def testLargestTwoChildren(self) -> None:
        self.assertEqual(self._numTree.largestValue(), 104)

    def testLargestRightHook(self) -> None:
        self.assertEqual(cast(BST[str], self._bothSidesNow.left()).largestValue(), 'garbage')

    def testLargestLeftHook(self) -> None:
        self.assertEqual(cast(BST[int], self._numTree.left()).largestValue(), 38)

    def testContainsWrongData(self) -> None:
        self.assertFalse('trash' in self._1item)

    def testContainsRoot(self) -> None:
        self.assertTrue('garbage' in self._1item)

    def testContainsWrongDataL(self) -> None:
        self.assertFalse('trash' in self._L1tree)

    def testContainsLChild(self) -> None:
        self.assertTrue('garbage' in self._L1tree)

    def testContainsWrongDataR(self) -> None:
        self.assertFalse('trash' in self._R1tree)

    def testContainsRChild(self) -> None:
        self.assertTrue('garbage' in self._R1tree)

    def testFindWrongData(self) -> None:
        with self.assertRaises(ValueError):
            self._1item.find('trash')

    def testFindRoot(self) -> None:
        self.assertEqual(self._1item.find('garbage'), self._1item)

    def testFindWrongDataL(self) -> None:
        with self.assertRaises(ValueError):
            self._L1tree.find('four')

    def testFindLChild(self) -> None:
        self.assertEqual(self._L1tree.find('five'), self._L1tree.left())

    def testFindWrongDataR(self) -> None:
        with self.assertRaises(ValueError):
            self._R1tree.find('trash')

    def testFindRChild(self) -> None:
        self.assertEqual(self._R1tree.find('garbage'), self._R1tree.right())

    def testLen(self) -> None:
        self.assertEqual(len(self._1item), 1)
        self.assertEqual(len(self._L1tree), 2)
        self.assertEqual(len(self._R1tree), 2)
        self.assertEqual(len(self._bothSidesNow), 4)

    def testHeight(self) -> None:
        self.assertEqual(self._1item.height(), 1)
        self.assertEqual(self._L1tree.height(), 2)
        self.assertEqual(self._R1tree.height(), 2)
        self.assertEqual(self._bothSidesNow.height(), 3)

    def testIter(self) -> None:
        self.assertEqual(list(iter(self._1item)), ['garbage'])
        self.assertEqual(list(iter(self._L1tree)), ['five', 'garbage'])
        self.assertEqual(list(iter(self._R1tree)), ['five', 'garbage'])
        self.assertEqual(list(iter(self._bothSidesNow)), ['five', 'garbage', 'infinity', 'left'])
        self.assertEqual(list(iter(self._numTree)), [13, 26, 28, 38, 55, 66, 70, 82, 104])

    def testPreorder(self) -> None:
        self.assertEqual(list(self._1item.preorder()), ['garbage'])
        self.assertEqual(list(self._L1tree.preorder()), ['garbage', 'five'])
        self.assertEqual(list(self._R1tree.preorder()), ['five', 'garbage'])
        self.assertEqual(list(self._bothSidesNow.preorder()), ['infinity', 'five', 'garbage', 'left'])
        self.assertEqual(list(self._numTree.preorder()), [55, 26, 13, 38, 28, 66, 82, 70, 104])

    def testBfPreorder(self) -> None:
        self.assertEqual(list(self._1item.bf_preorder()), ['garbage'])
        self.assertEqual(list(self._L1tree.bf_preorder()), ['garbage', 'five'])
        self.assertEqual(list(self._R1tree.bf_preorder()), ['five', 'garbage'])
        self.assertEqual(list(self._bothSidesNow.bf_preorder()), ['infinity', 'five', 'left', 'garbage'])
        self.assertEqual(list(self._numTree.bf_preorder()), [55, 26, 66, 13, 38, 82, 28, 70, 104])

    # def testInorder(self) -> None:
    #     self.assertEqual(list(self._1item.inorder()), ['garbage'])
    #     self.assertEqual(list(self._L1tree.inorder()), ['five', 'garbage'])
    #     self.assertEqual(list(self._R1tree.inorder()), ['five', 'garbage'])
    #     self.assertEqual(list(self._bothSidesNow.inorder()), ['five', 'garbage', 'infinity', 'left'])
    #     self.assertEqual(list(self._numTree.inorder()), [13, 26, 28, 38, 55, 66, 70, 82, 104])

    # Successor with a right child

    def testSuccessor55(self) -> None:
        self.assertEqual(self._numTree.successorValueRChild(), 66)

    def testSuccessor26(self) -> None:
        self.assertEqual(cast(BST[int], self._numTree.left()).successorValueRChild(), 28)

    def testSuccessor66(self) -> None:
        self.assertEqual(cast(BST[int], self._numTree.right()).successorValueRChild(), 70)

    def testSuccessor82(self) -> None:
        self.assertEqual(cast(BST[int], self._numTree.right().right()).successorValueRChild(), 104)

    # General successor

    # def testGeneralSuccessor(self) -> None:
    #     values: list[int] = list(iter(self._numTree))
    #     for i in range(1,len(values)):
    #         with self.subTest(i=i, val=values[i]):
    #             self.assertEqual(self._numTree.find(values[i-1]).generalSuccessor(), 
    #                               self._numTree.find(values[i]))

    def testSetLeftSubtreeException(self) -> None:
        with self.assertRaises(AssertionError):
            self._L1tree.setLeft('echo')

    def testSetLeftValueException(self) -> None:
        with self.assertRaises(ValueError):
            self._1item.setLeft('trash') # Should be added on right, not left

    def testSetLeftDuplicateException(self) -> None:
        with self.assertRaises(ValueError):
            self._1item.setLeft('garbage') # Already in that tree

    def testSetRightSubtreeException(self) -> None:
        with self.assertRaises(AssertionError):
            self._R1tree.setRight('whiskey')

    def testSetRightValueException(self) -> None:
        with self.assertRaises(ValueError):
            self._1item.setRight('foxtrot') # Should be added on left, not right

    def testSetRightDuplicateException(self) -> None:
        with self.assertRaises(ValueError):
            self._1item.setRight('garbage') # Already in that tree

    def testRemoveLeft(self) -> None:
        self._L1tree.removeLeft()           # Remove the 'five'
        self.assertEqual(list(iter(self._L1tree)), ['garbage'])
        self._R1tree.removeLeft()           # Nothing happens
        self.assertEqual(list(iter(self._R1tree)), ['five', 'garbage'])
        self._bothSidesNow.removeLeft()     # Removes the 'five' subtree
        self.assertEqual(list(iter(self._bothSidesNow)), ['infinity', 'left'])
        self._numTree.left().removeLeft()   # Removes 13
        self.assertEqual(list(iter(self._numTree)), [26, 28, 38, 55, 66, 70, 82, 104])

    def testRemoveRight(self) -> None:
        self._L1tree.removeRight()           # Nothing happens
        self.assertEqual(list(iter(self._L1tree)), ['five', 'garbage'])
        self._R1tree.removeRight()           # Remove the 'garbage'
        self.assertEqual(list(iter(self._R1tree)), ['five'])
        self._bothSidesNow.removeRight()     # Removes 'left'
        self.assertEqual(list(iter(self._bothSidesNow)), ['five', 'garbage', 'infinity'])
        self._numTree.right().removeRight()  # Removes the subtree rooted at 70
        self.assertEqual(list(iter(self._numTree)), [13, 26, 28, 38, 55, 66])

    # Remove by value

    def testRemoveLeaf(self) -> None:
        self._bothSidesNow = self._bothSidesNow.remove('garbage')       # type: ignore
        self.assertEqual(list(iter(self._bothSidesNow)), ['five', 'infinity', 'left'])
        # Verify structure
        self.assertEqual(self._bothSidesNow.data(), 'infinity')
        self.assertEqual(self._bothSidesNow.left().data(), 'five')
        self.assertEqual(self._bothSidesNow.right().data(), 'left')
        self.assertFalse(self._bothSidesNow.left().hasRightChild())

    def testRemoveRoot(self) -> None:
        self._L1tree = self._L1tree.remove('garbage')       # type: ignore
        self.assertEqual(self._L1tree.data(), 'five')
        self.assertFalse(self._L1tree.hasLeftChild())
        self.assertFalse(self._L1tree.hasRightChild())

    def testRemove1ChildLeft(self) -> None:
        self._numtree = self._numTree.remove(38)
        self.assertEqual(list(iter(self._numTree)), [13, 26, 28, 55, 66, 70, 82, 104])
        # Verify structure
        self.assertEqual(self._numTree.left().data(), 26)
        self.assertEqual(self._numTree.left().right().data(), 28)
        self.assertFalse(self._numTree.left().right().hasLeftChild())
        self.assertFalse(self._numTree.left().right().hasRightChild())

    def testRemove1ChildRight(self) -> None:
        self._numTree = self._numTree.remove(66)        # type: ignore
        self.assertEqual(list(iter(self._numTree)), [13, 26, 28, 38, 55, 70, 82, 104])
        # Verify structure
        self.assertEqual(self._numTree.right().data(), 82)
        self.assertEqual(self._numTree.right().left().data(), 70)
        self.assertEqual(self._numTree.right().right().data(), 104)

    def testRemove2Children(self) -> None:
        self._numTree = self._numTree.remove(26)        # type: ignore
        self.assertEqual(list(iter(self._numTree)), [13, 28, 38, 55, 66, 70, 82, 104])
        # Verify structure
        self.assertEqual(self._numTree.left().data(), 28)
        self.assertEqual(self._numTree.left().left().data(), 13)
        self.assertEqual(self._numTree.left().right().data(), 38)
        self.assertFalse(self._numTree.left().right().hasLeftChild())



if __name__ == '__main__':
    unittest.main()

