import unittest
from balanced_symbols import BalancedSymbols


class TestBalancedSymbols(unittest.TestCase):
    def test_balanced_case_1(self):
        input = "([{}])"
        self.assertEqual(BalancedSymbols(input), True)

    def test_balanced_case_2(self):
        input = "()()[]{}"
        self.assertEqual(BalancedSymbols(input), True)

    def test_balanced_case_3(self):
        input = "(()()[]{})"
        self.assertEqual(BalancedSymbols(input), True)

    def test_balanced_case_4(self):
        input = "(((((((((()))())))))))"
        self.assertEqual(BalancedSymbols(input), True)

    def test_unbalanced_case_1(self):
        input = "(((((((((()))()))))))"
        self.assertEqual(BalancedSymbols(input), False)

    def test_unbalanced_case_2(self):
        input = "()[]{)"
        self.assertEqual(BalancedSymbols(input), False)

    def test_unbalanced_case_3(self):
        input = "[{(]})"
        self.assertEqual(BalancedSymbols(input), False)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
