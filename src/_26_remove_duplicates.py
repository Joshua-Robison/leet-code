"""
Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        repeats = 0
        n = len(nums)
        for i in range(n - 1, 0, -1):
            if nums[i] == nums[i - 1]:
                del nums[i]
                repeats += 1
        return n - repeats
