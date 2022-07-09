"""Given a roman numeral, convert it to an integer."""
import unittest


class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for a, b in zip(s, s[1:]):
            if d[a] < d[b]:
                total -= d[a]
            else:
                total += d[a]
        return total + d[s[-1]]


class TestSolution(unittest.TestCase):
    def test_romanToInt(self):
        solution = Solution()
        s = "MCMXCIV"
        expected = 1994
        output = solution.romanToInt(s)
        self.assertTrue(expected, output)


if __name__ == "__main__":
    unittest.main()
