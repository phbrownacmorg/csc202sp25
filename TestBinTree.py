import unittest
from BinTree import BinTree
# import the code you want to test here

class TestBinTree(unittest.TestCase):

    def setUp(self) -> None:
        self._empty = BinTree[str]()

        self._1item = BinTree[str]('garbage')

        self._L1tree = BinTree[str]('five')                 #        five
        self._L1tree.setLeft('garbage')                     #        /
                                                            #   garbage

        self._R1tree = BinTree[str]('five')                 #       five
        self._R1tree.setRight('garbage')                    #          \
                                                            #           garbage

        self._bothSidesNow = BinTree[str]('infinity')       #       infinity
        self._bothSidesNow.setLeft('five')                  #        /    \
        self._bothSidesNow.left().setRight('garbage')       #     five    left
        self._bothSidesNow.setRight('left')                 #        \
                                                            #       garbage                                                         

        self._numTree = BinTree[int](55)                    #         55
        self._numTree.setLeft(26)                           #        /  \
        self._numTree.setRight(66)                          #      26    66
        self._numTree.left().setLeft(13)                    #     /  \     \
        self._numTree.left().setRight(38)                   #   13    38    82
        self._numTree.right().setRight(82)                  #        /     /  \
        self._numTree.left().right().setLeft(28)            #      28    70    104
        self._numTree.right().right().setLeft(70)
        self._numTree.right().right().setRight(104)

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testEmptyTrue(self) -> None:
        self.assertTrue(self._empty.empty())

    def testEmptyFalse(self) -> None:
        self.assertFalse(self._1item.empty())

    def testContainsEmpty(self) -> None:
        self.assertFalse('garbage' in self._empty)

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

    def testLen(self) -> None:
        self.assertEqual(len(self._empty), 0)
        self.assertEqual(len(self._1item), 1)
        self.assertEqual(len(self._L1tree), 2)
        self.assertEqual(len(self._R1tree), 2)
        self.assertEqual(len(self._bothSidesNow), 4)

    def testHeight(self) -> None:
        self.assertEqual(self._empty.height(), 0)
        self.assertEqual(self._1item.height(), 1)
        self.assertEqual(self._L1tree.height(), 2)
        self.assertEqual(self._R1tree.height(), 2)
        self.assertEqual(self._bothSidesNow.height(), 3)

    def testIter(self) -> None:
        self.assertEqual(list(iter(self._empty)), [])
        self.assertEqual(list(iter(self._1item)), ['garbage'])
        self.assertEqual(list(iter(self._L1tree)), ['garbage', 'five'])
        self.assertEqual(list(iter(self._R1tree)), ['five', 'garbage'])
        self.assertEqual(list(iter(self._bothSidesNow)), ['five', 'garbage', 'infinity', 'left'])
        self.assertEqual(list(iter(self._numTree)), [13, 26, 28, 38, 55, 66, 70, 82, 104])

    # def testPreorder(self) -> None:
    #     self.assertEqual(list(self._empty.preorder()), [])
    #     self.assertEqual(list(self._1item.preorder()), ['garbage'])
    #     self.assertEqual(list(self._L1tree.preorder()), ['five', 'garbage'])
    #     self.assertEqual(list(self._R1tree.preorder()), ['five', 'garbage'])
    #     self.assertEqual(list(self._bothSidesNow.preorder()), ['infinity', 'five', 'garbage', 'left'])
    #     self.assertEqual(list(self._numTree.preorder()), [55, 26, 13, 38, 28, 66, 82, 70, 104])

    def testRemoveLeft(self) -> None:
        self._empty.removeLeft()            # Nothing happens
        self.assertEqual(list(iter(self._empty)), [])
        self._L1tree.removeLeft()           # Remove the 'garbage'
        self.assertEqual(list(iter(self._L1tree)), ['five'])
        self._R1tree.removeLeft()           # Nothing happens
        self.assertEqual(list(iter(self._R1tree)), ['five', 'garbage'])
        self._bothSidesNow.removeLeft()     # Removes the 'five' subtree
        self.assertEqual(list(iter(self._bothSidesNow)), ['infinity', 'left'])
        self._numTree.left().removeLeft()   # Removes 13
        self.assertEqual(list(iter(self._numTree)), [26, 28, 38, 55, 66, 70, 82, 104])

    def testRemoveRight(self) -> None:
        self._empty.removeRight()            # Nothing happens
        self.assertEqual(list(iter(self._empty)), [])
        self._L1tree.removeRight()           # Nothing happens
        self.assertEqual(list(iter(self._L1tree)), ['garbage', 'five'])
        self._R1tree.removeRight()           # Remove the 'garbage'
        self.assertEqual(list(iter(self._R1tree)), ['five'])
        self._bothSidesNow.removeRight()     # Removes 'left'
        self.assertEqual(list(iter(self._bothSidesNow)), ['five', 'garbage', 'infinity'])
        self._numTree.right().removeRight()  # Removes the subtree rooted at 70
        self.assertEqual(list(iter(self._numTree)), [13, 26, 28, 38, 55, 66])

if __name__ == '__main__':
    unittest.main()

