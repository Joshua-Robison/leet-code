"""
You are climbing a staircase.
It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?
"""
import unittest


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 1] + [0] * (n - 1)
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


class TestSolution(unittest.TestCase):
    def test_climbStairs(self):
        solution = Solution()
        n = 3
        expected = 3
        output = solution.climbStairs(n)
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
