import unittest
from src._1_two_sum import Solution


class TestSolution(unittest.TestCase):
    def test_twoSum(self):
        nums, target = [2, 7, 11, 15], 9
        expected = [0, 1]
        output = Solution().twoSum(nums, target)
        self.assertEqual(output, expected)
