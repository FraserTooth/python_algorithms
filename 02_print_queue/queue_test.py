import unittest
from queue import Queue


class TestStack(unittest.TestCase):
    def test_enqueue(self):
        q = Queue()
        self.assertEqual(q.items, [])
        q.enqueue(1)
        self.assertEqual(q.items, [1])
        q.enqueue("fish")
        self.assertEqual(q.items, ["fish", 1])

    def test_dequeue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue("fish")
        self.assertEqual(q.items, ["fish", 1])
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.items, ["fish"])

    def test_dequeue_empty(self):
        q = Queue()
        self.assertEqual(q.dequeue(), None)

    def test_peek(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue("fish")
        q.enqueue(2)
        self.assertEqual(q.items, [2, "fish", 1])
        self.assertEqual(q.peek(), 1)

    def test_peek_empty(self):
        q = Queue()
        self.assertEqual(q.peek(), None)

    def test_size(self):
        q = Queue()
        self.assertEqual(q.size(), 0)
        q.enqueue(1)
        self.assertEqual(q.size(), 1)
        q.enqueue("fish")
        self.assertEqual(q.size(), 2)
        q.enqueue(2)
        self.assertEqual(q.size(), 3)

    def test_is_empty(self):
        q = Queue()
        self.assertEqual(q.is_empty(), True)
        q.enqueue(1)
        self.assertEqual(q.is_empty(), False)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
