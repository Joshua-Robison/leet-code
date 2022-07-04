import unittest
from src._4_median_two_arrays import Solution


class TestSolution(unittest.TestCase):
    def test_findMedianSortedArrays(self):
        nums1, nums2 = [1, 2], [3, 4]
        expected = 2.5
        output = Solution().findMedianSortedArrays(nums1, nums2)
        self.assertEqual(output, expected)
