"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = min([len(word) for word in strs])
        prefix = ""
        for i in range(n):
            letters = [word[i] for word in strs]
            if letters.count(letters[0]) == len(letters):
                prefix += letters[0]
            else:
                break

        return prefix
