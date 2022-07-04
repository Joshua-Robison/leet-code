import unittest
from src._15_3sum import Solution


class TestSolution(unittest.TestCase):
    def test_twoSum(self):
        nums = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, -1, 2], [-1, 0, 1]]
        output = Solution().threeSum(nums)
        self.assertEqual(output, expected)
