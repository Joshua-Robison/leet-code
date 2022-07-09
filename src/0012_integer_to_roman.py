"""Given an integer, convert it to a roman numeral."""
import unittest


class Solution:
    def intToRoman(self, num: int) -> str:
        s = []
        d = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
        for value, symbol in d:
            if num == 0:
                break
            count, num = divmod(num, value)
            s.append(symbol * count)
        return "".join(s)


class TestSolution(unittest.TestCase):
    def test_intToRoman(self):
        solution = Solution()
        num = 1994
        expected = "MCMXCIV"
        output = solution.intToRoman(num)
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
