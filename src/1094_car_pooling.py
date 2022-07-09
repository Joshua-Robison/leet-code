"""
There is a car with capacity empty seats.
The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where

    trips[i] = [numPassengers, from, to]

indicates that the ith trip has numPassengers passengers
and the locations to pick them up and drop them off are from and to respectively.
The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all
passengers for all the given trips, or false otherwise.
"""
import heapq
import unittest
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda trip: trip[1])
        tracker = []
        numPassengers = 0
        for trip in trips:
            ppl, start, stop = trip
            while tracker and tracker[0][0] <= start:
                numPassengers -= tracker[0][1]
                heapq.heappop(tracker)
            numPassengers += ppl
            if numPassengers > capacity:
                return False
            heapq.heappush(tracker, [stop, ppl])
        return True


class TestSolution(unittest.TestCase):
    def test_carPooling(self):
        solution = Solution()
        trips = [[2, 1, 5], [3, 3, 7]]
        capacity = 4
        output = solution.carPooling(trips, capacity)
        self.assertFalse(output)


if __name__ == "__main__":
    unittest.main()
