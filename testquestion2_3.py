import unittest
from question2_3 import SubArray

class TestSubArray(unittest.TestCase):
    pass
# question 2(a) -- Testing can be a word
    def testAdd(self):
        data = [2, 7, 9, 10, 5]
        forTest = SubArray.add(data)
        self.assertNotEqual(forTest, 12)

# question 2(b) -- Testing if the item is deleted
    def testdelete(self):
        data = [2, 7, 9, 10, 5]
        forTest = SubArray.delete(data)
        self.assertEqual(forTest, 5)

# Question Three
# question 3(a) -- Testing if the item is there
    def testcheck(self):
        data = [2, 7, 9, 10, 5]
        forTest = SubArray.check(data)
        self.assertEqual(forTest, 5)

# question 3(b) -- Testing if the reverse is correct
    def testreverse(self):
        data = [2, 7, 9, 10, 5]
        forTest = SubArray.reverse(data)
        self.assertNotEqual(forTest, data)

# question 3(c) -- Testing if the integer is inserted
    def testinsertion(self):
        data = [2, 7, 9, 10, 5]
        forTest = SubArray.insertion(data)
        self.assertEqual(forTest, 76)

if __name__ == "__main__":
    unittest.main()