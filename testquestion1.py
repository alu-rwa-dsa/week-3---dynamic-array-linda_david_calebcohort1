import unittest
from question1 import Array

class TestArray(unittest.TestCase):
    # question a -- Testing if length is strictly integer
    def testLength(self):
        data = [2, 7, 9, 10, 5]
        forTest = Array.length(data)
        self.assertEqual(forTest, 5)

    # question b -- Testing if the index is a number
    def testIndex(self):
        data = [2, 7, 9, 10, 5]
        forTest = Array.index(data)
        self.assertNotEqual(forTest, "dog")

    # Testing question c -- Testing if the position is correct
    def testReplace(self):
        data = [2, 7, 9, 10, 5]
        forTest = Array.replace(data)
        self.assertNotEqual(forTest, 23)

if __name__ == "__main__":
    unittest.main()
