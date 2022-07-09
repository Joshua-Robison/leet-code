"""
Given a string s containing just the characters

    '(', ')', '{', '}', '[' and ']'

determine if the input string is valid.
"""
import unittest


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(":
                stack.append(")")
            elif c == "{":
                stack.append("}")
            elif c == "[":
                stack.append("]")
            elif not stack or stack.pop() != c:
                return False
        return not stack


class TestSolution(unittest.TestCase):
    def test_isValid(self):
        solution = Solution()
        s = "()[]{}"
        output = solution.isValid(s)
        self.assertTrue(output)


if __name__ == "__main__":
    unittest.main()
