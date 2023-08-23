# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(next=head)
        pt, prev = head, dummyHead
        while pt is not None:
            next = pt.next
            pt.next = prev
            prev, pt = pt, next

        pt, prev = prev, None
        carry_over = 0
        while pt is not dummyHead:
            pt.val *= 2
            pt.val += carry_over
            carry_over = pt.val // 10
            pt.val %= 10

            next = pt.next
            pt.next = prev
            pt, prev = next, pt

        dummyHead.next = prev

        if carry_over > 0:
            dummyHead.next = ListNode(val=carry_over, next=prev)

        return dummyHead.next