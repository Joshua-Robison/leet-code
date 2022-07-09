"""Given a string s, find the length of the longest substring without repeating characters."""
import unittest
from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = l = 0
        count = Counter()
        for r, c in enumerate(s):
            count[c] += 1
            while count[c] > 1:
                count[s[l]] -= 1
                l += 1
            best = max(best, r - l + 1)
        return best


class TestSolution(unittest.TestCase):
    def test_lengthOfLongestSubstring(self):
        solution = Solution()
        s = "abcabcbb"
        expected = 3
        output = solution.lengthOfLongestSubstring(s)
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
