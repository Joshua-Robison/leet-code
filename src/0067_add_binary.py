"""Given two binary strings a and b, return their sum as a binary string."""
import unittest


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return format(int(a, 2) + int(b, 2), "b")


class TestSolution(unittest.TestCase):
    def test_addBinary(self):
        solution = Solution()
        a = "1010"
        b = "1011"
        expected = "10101"
        output = solution.addBinary(a, b)
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
