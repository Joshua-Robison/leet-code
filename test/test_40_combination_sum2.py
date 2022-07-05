import unittest
from src._40_combination_sum2 import Solution


class TestSolution(unittest.TestCase):
    def test_combinationSum2(self):
        candidates, target = [10, 1, 2, 7, 6, 1, 5], 8
        expected = sorted([[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]])
        output = sorted(Solution().combinationSum2(candidates, target))
        self.assertEqual(output, expected)
