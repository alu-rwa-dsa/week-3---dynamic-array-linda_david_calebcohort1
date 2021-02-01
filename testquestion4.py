import unittest
from question4 import Dictionary

class TestAssociation(unittest.TestCase):
# question 4(a) -- Testing if the method can add an item
    def testAddition(self):
        data = {"name": "Kamali", "age": 45}
        forTest = Dictionary.addition(data)
        self.assertNotEqual(forTest, "Karemera")

# question 4(b) -- Testing item is removed
    def testRemove(self):
        data = {"name": "Kamali", "age": 45}
        forTest = Dictionary.remove(data)
        self.assertEqual(forTest, "name")

# question 4(c) -- Testing if the dictionary was modified
    def testModify(self):
        data = {"name": "Kamali", "age": 45}
        forTest = Dictionary.modify(data)
        self.assertEqual(forTest, 40)

# question 4(d) -- Testing for checking an item
    def testLookup(self):
        data = {"name": "Kamali", "age": 45}
        forTest = Dictionary.lookup(data)
        self.assertEqual(forTest, 5)

if __name__ == "__main__":
    unittest.main()