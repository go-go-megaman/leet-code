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
        dummy_node = current = ListNode(0)
        carry = 0

        while l1 is not None or l2 is not None:
            value1 = l1.value if l1 is not None else 0
            value2 = l2.value if l2 is not None else 0
            sum = value1 + value2 + carry
            carry = 1 if sum >= 10 else 0
            current.next = ListNode(sum - 10 if sum >= 10 else sum)
            current = current.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        return dummy_node.next
