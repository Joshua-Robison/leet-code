import unittest
from src._6_zigzag_conversion import Solution


class TestSolution(unittest.TestCase):
    def test_convert(self):
        s, numRows = "PAYPALISHIRING", 3
        expected = "PAHNAPLSIIGYIR"
        output = Solution().convert(s, numRows)
        self.assertEqual(output, expected)
