"""Given a roman numeral, convert it to an integer."""


class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total, prev = 0, ""
        for i in range(len(s)):
            curr = s[i]
            if prev == "I" and (curr == "V" or curr == "X"):
                total -= 2 * d[prev]
            elif prev == "X" and (curr == "L" or curr == "C"):
                total -= 2 * d[prev]
            elif prev == "C" and (curr == "D" or curr == "M"):
                total -= 2 * d[prev]

            total += d[curr]
            prev = curr

        return total
