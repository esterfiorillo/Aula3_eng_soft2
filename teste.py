import unittest
from stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def testEmptyStack(self):
        self.setUp()
        self.assertEqual(True, self.stack.is_empty())

    def testNotEmptyStack(self):
        self.setUp()
        self.stack.push(1)
        self.assertEqual(False, self.stack.is_empty())

    def testSizeStack(self):
        self.setUp()
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertTrue(self.stack.size == 3)

    def testPushPopStack(self):
        self.setUp()
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        result = self.stack.pop()
        self.assertEqual(3, result)

    def testEmptyStackException(self):
      self.setUp()
      with self.assertRaises(Exception):
        
        self.stack.pop()

