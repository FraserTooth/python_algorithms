import unittest
from dequeue import Dequeue


class TestStack(unittest.TestCase):
    def test_add_front(self):
        d = Dequeue()
        self.assertEqual(d.items, [])
        d.add_front("apple")
        d.add_front("banana")
        self.assertEqual(d.items, ["banana", "apple"])

    def test_add_rear(self):
        d = Dequeue()
        self.assertEqual(d.items, [])
        d.add_rear("apple")
        d.add_rear("banana")
        self.assertEqual(d.items, ["apple", "banana"])

    def test_remove_front(self):
        d = Dequeue()
        d.add_front("apple")
        d.add_front("banana")
        d.add_front("cherry")
        self.assertEqual(d.remove_front(), "cherry")
        self.assertEqual(d.items, ["banana", "apple"])

    def test_remove_rear(self):
        d = Dequeue()
        d.add_front("apple")
        d.add_front("banana")
        d.add_front("cherry")
        self.assertEqual(d.remove_rear(), "apple")
        self.assertEqual(d.items, ["cherry", "banana"])

    def test_remove_empty(self):
        d = Dequeue()
        self.assertEqual(d.items, [])
        self.assertEqual(d.remove_front(), None)
        self.assertEqual(d.remove_rear(), None)

    def test_peek_front_rear(self):
        d = Dequeue()
        d.add_front("apple")
        d.add_front("banana")
        d.add_front("cherry")
        self.assertEqual(d.items, ["cherry", "banana", "apple"])
        self.assertEqual(d.peek_front(), "cherry")
        self.assertEqual(d.peek_rear(), "apple")

    def test_peek_empty(self):
        d = Dequeue()
        self.assertEqual(d.peek_front(), None)
        self.assertEqual(d.peek_rear(), None)

    def test_size(self):
        d = Dequeue()
        self.assertEqual(d.size(), 0)
        d.add_front("apple")
        self.assertEqual(d.size(), 1)
        d.add_front("banana")
        self.assertEqual(d.size(), 2)
        d.add_front("cherry")
        self.assertEqual(d.size(), 3)

    def test_is_empty(self):
        d = Dequeue()
        self.assertEqual(d.is_empty(), True)
        d.add_front("apple")
        self.assertEqual(d.is_empty(), False)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
