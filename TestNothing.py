import unittest
# import the code you want to test here

class TestNothing(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testTrue(self) -> None:
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()

