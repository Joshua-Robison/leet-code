"""
Given an array of integers heights representing the
histogram's bar height where the width of each bar is 1,
return the area of the largest rectangle in the histogram.
"""
import unittest
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = []
        for i in range(len(heights) + 1):
            while stack and (i == len(heights) or heights[stack[-1]] > heights[i]):
                h = heights[stack.pop()]
                w = i - stack[-1] - 1 if stack else i
                area = max(area, h * w)
            stack.append(i)
        return area


class TestSolution(unittest.TestCase):
    def test_largestRectangleArea(self):
        solution = Solution()
        heights = [2, 1, 5, 6, 2, 3]
        expected = 10
        output = solution.largestRectangleArea(heights)
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
