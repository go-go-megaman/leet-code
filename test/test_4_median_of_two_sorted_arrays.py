import unittest
from solutions._4_median_of_two_sorted_arrays import (
    Solution)


class TestMainMethod(unittest.TestCase):
    def test_when_the_sum_of_nums1_length_and_nums2_length_is_even(self):
        target = Solution()

        actual = target.main([4, 5, 8], [1, 2, 7])

        expected = 4.5
        self.assertEqual(actual, expected)

    def test_when_the_sum_of_nums1_length_and_nums2_length_is_odd(self):
        target = Solution()

        actual = target.main([1, 3, 5], [2, 4])

        expected = 3
        self.assertEqual(actual, expected)
