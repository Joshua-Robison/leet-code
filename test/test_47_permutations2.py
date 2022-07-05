import unittest
from src._47_permutations2 import Solution


class TestSolution(unittest.TestCase):
    def test_permuteUnique(self):
        nums = [1, 1, 2]
        expected = sorted([[1, 1, 2], [1, 2, 1], [2, 1, 1]])
        output = sorted(Solution().permuteUnique(nums))
        self.assertEqual(output, expected)
