import unittest
from src._14_longest_common_prefix import Solution


class TestSolution(unittest.TestCase):
    def test_longestCommonPrefix(self):
        strs, expected = ["flower", "flow", "flight"], "fl"
        output = Solution().longestCommonPrefix(strs)
        self.assertEqual(output, expected)
