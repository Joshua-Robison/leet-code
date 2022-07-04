import unittest
from src._3_longest_substring import Solution


class TestSolution(unittest.TestCase):
    def test_lengthOfLongestSubstring(self):
        s = "pwwkew"
        expected = 3
        output = Solution().lengthOfLongestSubstring(s)
        self.assertEqual(output, expected)
