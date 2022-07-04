"""Given an integer, convert it to a roman numeral."""


class Solution:
    def intToRoman(self, num: int) -> str:
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

        s = []
        for value, symbol in d:
            if num == 0:
                break
            count, num = divmod(num, value)
            s.append(symbol * count)

        return "".join(s)
