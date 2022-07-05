"""
Given n non-negative integers representing an elevation map where the
width of each bar is 1, compute how much water it can trap after raining.
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        if not height:
            return water

        n = len(height)
        l, r = 0, n - 1
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
