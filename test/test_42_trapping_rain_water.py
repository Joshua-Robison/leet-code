import unittest
from src._42_trapping_rain_water import Solution


class TestSolution(unittest.TestCase):
    def test_trap(self):
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        expected = 6
        output = Solution().trap(height)
        self.assertEqual(output, expected)
