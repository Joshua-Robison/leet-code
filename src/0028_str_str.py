"""
Given two strings needle and haystack,
return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.
"""
import unittest


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        for i in range(m - n + 1):
            if haystack[i : i + n] == needle:
                return i
        return -1


class TestSolution(unittest.TestCase):
    def test_strStr(self):
        solution = Solution()
        haystack = "hello"
        needle = "ll"
        expected = 2
        output = solution.strStr(haystack, needle)
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
