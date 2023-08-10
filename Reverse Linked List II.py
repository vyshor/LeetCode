# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head.next is None:
            return head

        left -= 1
        right -= 1
        reverse_count = right - left + 1
        if reverse_count == 0:
            return head

        dummy = ListNode(next=head)
        prev, pt = dummy, dummy.next
        for _ in range(left):
            pt, prev = pt.next, pt

        before_start = prev
        end = pt
        for _ in range(reverse_count):
            next = pt.next
            pt.next = prev
            prev, pt = pt, next

        before_start.next = prev
        end.next = pt

        return dummy.next


