import unittest
from src._27_remove_element import Solution


class TestSolution(unittest.TestCase):
    def test_removeElement(self):
        nums, val = [3, 2, 2, 3], 3
        expected = [2, 2]
        output = Solution().removeElement(nums, val)
        self.assertEqual(nums, expected)
        self.assertEqual(output, len(expected))
