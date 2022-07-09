"""Given an input string s, reverse the order of the words."""
import unittest


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


class TestSolution(unittest.TestCase):
    def test_reverseWords(self):
        solution = Solution()
        s = "a good   example"
        expected = "example good a"
        output = solution.reverseWords(s)
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
