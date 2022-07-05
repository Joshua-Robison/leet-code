import unittest
from src._26_remove_duplicates import Solution


class TestSolution(unittest.TestCase):
    def test_removeDuplicates(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        expected = [0, 1, 2, 3, 4]
        output = Solution().removeDuplicates(nums)
        self.assertEqual(nums, expected)
        self.assertEqual(output, len(expected))
