import unittest
from solutions._1_two_sum import Solution


class TestMainMethod(unittest.TestCase):
    def test_when_the_pair_exists(self):
        target = Solution()

        actual = target.main([1, 3, 5, 9, 2], 6)

        expected = [0, 2]
        self.assertListEqual(actual, expected)

    def test_when_the_pair_does_not_exist(self):
        with self.assertRaises(ValueError):
            Solution().main([1, 3, 5, 9, 2], 100)
