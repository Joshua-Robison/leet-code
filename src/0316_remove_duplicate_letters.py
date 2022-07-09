"""
Given a string s, remove duplicate letters so
that every letter appears once and only once.
You must make sure your result is the smallest in
lexicographical order among all possible results.
"""
import unittest
from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        res = []
        count = Counter(s)
        used = [False] * 26
        for c in s:
            count[c] -= 1
            if used[ord(c) - ord("a")]:
                continue
            while res and res[-1] > c and count[res[-1]] > 0:
                used[ord(res[-1]) - ord("a")] = False
                res.pop()
            res.append(c)
            used[ord(res[-1]) - ord("a")] = True
        return "".join(res)


class TestSolution(unittest.TestCase):
    def test_removeDuplicateLetters(self):
        solution = Solution()
        s = "cbacdcbc"
        expected = "acdb"
        output = solution.removeDuplicateLetters(s)
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
