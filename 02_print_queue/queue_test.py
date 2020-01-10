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


if __name__ == "__main__":
    unittest.main()
