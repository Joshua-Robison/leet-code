import unittest
from src._35_search_insert_position import Solution


class TestSolution(unittest.TestCase):
    def test_searchInsert(self):
        nums, target = [1, 3, 5, 6], 2
        expected = 1
        output = Solution().searchInsert(nums, target)
        self.assertEqual(output, expected)
