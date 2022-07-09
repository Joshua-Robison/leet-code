"""Given a string s, return the longest palindromic substring in s."""
import unittest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        best, bestLen = "", 0
        for i in range(n):
            # odd length
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > bestLen:
                    best = s[l : r + 1]
                    bestLen = r - l + 1
                l -= 1
                r += 1
            # even length
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > bestLen:
                    best = s[l : r + 1]
                    bestLen = r - l + 1
                l -= 1
                r += 1
        return best


class TestSolution(unittest.TestCase):
    def test_longestPalindrome(self):
        solution = Solution()
        s = "babad"
        expected = "bab"
        output = solution.longestPalindrome(s)
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
