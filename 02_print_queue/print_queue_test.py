import unittest
from print_queue import Job, Printer


class TestStack(unittest.TestCase):
    def test_enqueue(self):
        q = Queue()
        self.assertEqual(q.items, [])
        q.enqueue(1)
        self.assertEqual(q.items, [1])
        q.enqueue("fish")
        self.assertEqual(q.items, ["fish", 1])


if __name__ == "__main__":
    unittest.main()
