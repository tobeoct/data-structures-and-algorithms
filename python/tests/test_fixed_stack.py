import unittest

from data_structures.linear.stack.fixed_stack import Stack as FixedStack

class TestFixedStack(unittest.TestCase):
    
    def test_initialization(self):
        stack = FixedStack(size=3)
        self.assertEqual(stack.size(), 3)
        self.assertEqual(stack.count(), 0)
    
    def test_push(self):
        stack = FixedStack(size=2)
        stack.push(1)
        self.assertEqual(stack.count(), 1)
        self.assertFalse(stack.is_full())
        stack.push(2)
        self.assertEqual(stack.count(), 2)
        self.assertTrue(stack.is_full())
        with self.assertRaises(OverflowError):
            stack.push(3)  # FixedStack is full, should raise an OverflowError
    
    def test_pop(self):
        stack = FixedStack(size=2)
        self.assertIsNone(stack.pop())  # FixedStack is empty, should return None
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertIsNone(stack.pop())  # FixedStack is empty again, should return None
    
    def test_is_full(self):
        stack = FixedStack(size=1)
        self.assertFalse(stack.is_full())
        stack.push(1)
        self.assertTrue(stack.is_full())
    
    def test_is_empty(self):
        stack = FixedStack(size=1)
        self.assertTrue(stack.is_empty())
        stack.push(1)
        self.assertFalse(stack.is_empty())
    
    def test_peek(self):
        stack = FixedStack(size=2)
        self.assertIsNone(stack.peek())  # FixedStack is empty, should return None
        stack.push(1)
        self.assertEqual(stack.peek(), 1)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)
        stack.pop()
        self.assertEqual(stack.peek(), 1)


