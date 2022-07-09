"""Insert description here."""
import unittest
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            cur = "Fizz" if i % 3 == 0 else ""
            cur += "Buzz" if i % 5 == 0 else ""
            if not cur:
                res.append(str(i))
            else:
                res.append(cur)
        return res


class TestSolution(unittest.TestCase):
    def test_fizzBuzz(self):
        solution = Solution()
        n = 5
        expected = ["1", "2", "Fizz", "4", "Buzz"]
        output = solution.fizzBuzz(n)
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
