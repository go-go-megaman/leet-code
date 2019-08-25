import unittest
from solutions._1_two_sum import Solution


class TestMainMethod(unittest.TestCase):
    def test_exists_pair_their_sum_equal_to_the_target(self):
        target = Solution()

        actual = target.main([1, 3, 5, 9, 2], 6)

        expected = [1, 5]
        self.assertListEqual(actual, expected)

    def test_does_not_exist_pair_their_sum_equal_to_the_target(self):
        with self.assertRaises(ValueError):
            Solution().main([1, 3, 5, 9, 2], 100)
