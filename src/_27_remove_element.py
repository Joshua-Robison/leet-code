"""
Given an integer array nums and an integer val,
remove all occurrences of val in nums in-place.
The relative order of the elements may be changed.
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        hits = 0
        n = len(nums)
        for i in range(n - 1, -1, -1):
            if nums[i] == val:
                del nums[i]
                hits += 1
        return n - hits
