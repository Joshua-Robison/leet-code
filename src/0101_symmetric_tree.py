"""
Given the root of a binary tree,
check whether it is a mirror of itself
(i.e., symmetric around its center).
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSymmetric(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p or not q:
                return p == q
            return (
                p.val == q.val
                and isSymmetric(p.left, q.right)
                and isSymmetric(p.right, q.left)
            )

        return isSymmetric(root, root)


if __name__ == "__main__":
    pass
