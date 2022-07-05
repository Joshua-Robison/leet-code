import unittest
from src._46_permutations import Solution


class TestSolution(unittest.TestCase):
    def test_permute(self):
        nums = [1, 2, 3]
        expected = sorted(
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        )
        output = sorted(Solution().permute(nums))
        self.assertEqual(output, expected)
