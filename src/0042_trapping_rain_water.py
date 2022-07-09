"""
Given n non-negative integers representing an elevation map where the
width of each bar is 1, compute how much water it can trap after raining.
"""
import unittest
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        if not height:
            return water
        l, r = 0, len(height) - 1
        maxLeft = height[l]
        maxRight = height[r]
        while l < r:
            if maxLeft < maxRight:
                water += maxLeft - height[l]
                l += 1
                maxLeft = max(maxLeft, height[l])
            else:
                water += maxRight - height[r]
                r -= 1
                maxRight = max(maxRight, height[r])
        return water


class TestSolution(unittest.TestCase):
    def test_trap(self):
        solution = Solution()
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        expected = 6
        output = solution.trap(height)
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
