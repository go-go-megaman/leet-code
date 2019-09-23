import unittest
from solutions._3_longest_substring_without_repeating_characters import (
    Solution)


class TestMainMethod(unittest.TestCase):
    def test_when_the_longest_substring_is_the_first_substring_of_argument(
            self):
        target = Solution()

        actual = target.main('abcabcbb')

        expected = 3
        self.assertEqual(actual, expected)

    def test_when_the_longest_substring_is_not_the_first_substring_of_argument(
            self):
        target = Solution()

        actual = target.main('pwwkew')

        expected = 3
        self.assertEqual(actual, expected)

    def test_when_the_argument_contains_only_one_character(
            self):
        target = Solution()

        actual = target.main('aaaaaaaaaaaaaaaaa')

        expected = 1
        self.assertEqual(actual, expected)
