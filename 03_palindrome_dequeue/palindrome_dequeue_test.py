import unittest
from palindrome_dequeue import PalindromeDetector


class TestStack(unittest.TestCase):
    def test_short_word_true(self):
        self.assertEqual(PalindromeDetector("mom"), True)
        self.assertEqual(PalindromeDetector("bab"), True)
        self.assertEqual(PalindromeDetector("taat"), True)
        self.assertEqual(PalindromeDetector("nn"), True)

    def test_short_word_false(self):
        self.assertEqual(PalindromeDetector("mob"), False)
        self.assertEqual(PalindromeDetector("bat"), False)
        self.assertEqual(PalindromeDetector("teat"), False)
        self.assertEqual(PalindromeDetector("ni"), False)

    def test_classic(self):
        self.assertEqual(PalindromeDetector("racecar"), True)
        self.assertEqual(PalindromeDetector("radar"), True)
        self.assertEqual(PalindromeDetector("madam"), True)
        self.assertEqual(PalindromeDetector("kayak"), True)
        self.assertEqual(PalindromeDetector("murmur"), False)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
