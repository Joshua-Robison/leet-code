"""Given an integer n, return the number of prime numbers that are strictly less than n."""
import unittest


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        isPrime = [False] * 2 + [True] * (n - 2)
        for i in range(2, int(n / 2) + 1):
            if isPrime[i]:
                for j in range(i * i, n, i):
                    isPrime[j] = False
        return sum(isPrime)


class TestSolution(unittest.TestCase):
    def test_countPrimes(self):
        solution = Solution()
        n = 10
        expected = 4
        output = solution.countPrimes(n)
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
