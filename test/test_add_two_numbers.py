import unittest
from solutions._2_add_two_numbers import Solution, ListNode


class TestMainMethod(unittest.TestCase):
    def test_add_the_two_numbers_and_return_it_as_a_list_node(self):
        target = Solution()
        test_node1 = self.createTestNode([2, 4, 3])
        test_node2 = self.createTestNode([5, 6, 4])

        result = target.main(test_node1, test_node2)
        actual = result.toList()

        expected = [7, 0, 8]
        self.assertListEqual(actual, expected)

    def test_add_two_numbers_with_different_digits(self):
        target = Solution()
        test_node1 = self.createTestNode([2])
        test_node2 = self.createTestNode([5, 6, 4])

        result = target.main(test_node1, test_node2)
        actual = result.toList()

        expected = [7, 6, 4]
        self.assertListEqual(actual, expected)

    def test_when_sum_get_extra_carry_at_the_end(self):
        target = Solution()
        test_node1 = self.createTestNode([0, 9])
        test_node2 = self.createTestNode([0, 1])

        result = target.main(test_node1, test_node2)
        actual = result.toList()

        expected = [0, 0, 1]
        self.assertListEqual(actual, expected)

    def createTestNode(self, numberList: [int]) -> ListNode:
        first = current = ListNode(numberList[0])
        for number in numberList[1:]:
            current.next = ListNode(number)
            current = current.next
        return first
