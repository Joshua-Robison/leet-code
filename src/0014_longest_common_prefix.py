"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""
import unittest
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if not strs:
            return prefix
        n = min([len(s) for s in strs])
        for i in range(n):
            letters = set([s[i] for s in strs])
            if len(letters) != 1:
                break
            prefix += letters.pop()
        return prefix


class TestSolution(unittest.TestCase):
    def test_longestCommonPrefix(self):
        solution = Solution()
        strs = ["flower", "flow", "flight"]
        expected = "fl"
        output = solution.longestCommonPrefix(strs)
        self.assertTrue(expected, output)


if __name__ == "__main__":
    unittest.main()
