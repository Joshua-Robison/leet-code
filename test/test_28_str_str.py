import unittest
from src._28_str_str import Solution


class TestSolution(unittest.TestCase):
    def test_strStr(self):
        haystack, needle = "hello", "ll"
        expected = 2
        output = Solution().strStr(haystack, needle)
        self.assertEqual(output, expected)
