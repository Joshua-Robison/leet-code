import unittest
from src._39_combination_sum import Solution


class TestSolution(unittest.TestCase):
    def test_combinationSum(self):
        candidates, target = [2, 3, 6, 7], 7
        expected = sorted([[2, 2, 3], [7]])
        output = sorted(Solution().combinationSum(candidates, target))
        self.assertEqual(output, expected)
