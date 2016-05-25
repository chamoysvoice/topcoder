from __future__ import division
import unittest


class GerrymenderEasy:
    @staticmethod
    def getmax(A, B, k):
        max_ratio = 0
        for i in xrange(len(A) - k):
            a = i
            b = k + i - 1
            while b < len(A):
                ratio = sum([B[t] for t in xrange(a, b + 1)]) / sum([A[t] for t in xrange(a, b + 1)])
                if ratio > max_ratio:
                    max_ratio = ratio
                b += 1
        return max_ratio


class TestGerrymenderEasy(unittest.TestCase):
    def test_one(self):
        self.assertEqual(0.75, GerrymenderEasy.getmax([5, 1, 2, 7], [4, 0, 2, 2], 2))

    def test_two(self):
        self.assertAlmostEqual(0.0833333, GerrymenderEasy.getmax([12, 34, 56, 78, 90], [1, 1, 1, 1, 1], 1))

    def test_three(self):
        self.assertAlmostEqual(0.00054, GerrymenderEasy.getmax(
            [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],
            [3, 1, 4, 1, 5, 9, 2, 6, 5, 3], 5))

    def test_four(self):
        self.assertEqual(0, GerrymenderEasy.getmax(
            [123, 4, 46, 88, 22, 34, 564, 87, 56, 311, 886],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 1))
