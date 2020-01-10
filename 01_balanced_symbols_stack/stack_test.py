import unittest
from stack import Stack


class TestStack(unittest.TestCase):
    def test_push(self):
        input = Stack()
        self.assertEqual(input.items, [])
        input.push(1)
        self.assertEqual(input.items, [1])
        input.push("fish")
        self.assertEqual(input.items, [1, "fish"])

    def test_pop(self):
        input = Stack()
        input.push(1)
        input.push("fish")
        self.assertEqual(input.items, [1, "fish"])
        self.assertEqual(input.pop(), "fish")
        self.assertEqual(input.items, [1])

    def test_pop_empty_list(self):
        input = Stack()
        self.assertEqual(input.pop(), None)

    def test_peek(self):
        input = Stack()
        input.push(1)
        input.push("fish")
        self.assertEqual(input.items, [1, "fish"])
        self.assertEqual(input.peek(), "fish")
        self.assertEqual(input.items, [1, "fish"])

    def test_peek_empty_list(self):
        input = Stack()
        self.assertEqual(input.peek(), None)

    def test_size(self):
        input = Stack()
        self.assertEqual(input.size(), 0)
        input.push(1)
        self.assertEqual(input.size(), 1)
        input.push("fish")
        self.assertEqual(input.size(), 2)

    def test_is_empty(self):
        input = Stack()
        self.assertEqual(input.is_empty(), True)
        input.push(1)
        self.assertEqual(input.is_empty(), False)
        input.push("fish")
        self.assertEqual(input.is_empty(), False)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
