class ListNode:
    def __init__(self, value: int):
        self.value: int = value
        self.next: ListNode = None

    def toList(self) -> [int]:
        result = [self.value]
        current = self
        while current.next:
            current = current.next
            result.append(current.value)
        return result


class Solution:
    def main(self, l1: ListNode, l2: ListNode) -> ListNode:
        (current_node, has_carry) = self.sum(l1, l2, False)
        first_node = current_node

        while l1.next is not None:
            l1 = l1.next
            l2 = l2.next
            previous_node = current_node
            (current_node, has_carry) = self.sum(l1, l2, has_carry)
            previous_node.next = current_node

        return first_node

    def sum(self, l1: ListNode, l2: ListNode,
            previous_digit_has_carry: bool) -> (ListNode, bool):
        result = l1.value + l2.value + int(previous_digit_has_carry)
        has_carray = result >= 10
        if has_carray:
            return (ListNode(result - 10), has_carray)
        return (ListNode(result), has_carray)
