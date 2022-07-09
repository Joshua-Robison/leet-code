"""Given n, calculate F(n)."""
import unittest


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        one, two = 0, 1
        for _ in range(2, n):
            temp = two
            two = one + two
            one = temp
        return one + two


class TestSolution(unittest.TestCase):
    def test_fib(self):
        solution = Solution()
        n = 5
        expected = 5
        output = solution.fib(n)
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
