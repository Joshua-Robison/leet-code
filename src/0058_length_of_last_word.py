"""
Given a string s consisting of words and spaces,
return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""
import unittest


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


class TestSolution(unittest.TestCase):
    def test_lengthOfLastWord(self):
        solution = Solution()
        s = "Hello World"
        expected = 5
        output = solution.lengthOfLastWord(s)
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
