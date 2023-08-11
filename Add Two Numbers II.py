# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy1, dummy2 = ListNode(next=l1), ListNode(next=l2)
        prev, pt = dummy1, dummy1.next
        while pt is not None:
            next = pt.next
            pt.next = prev
            prev, pt = pt, next

        end1 = prev

        prev, pt = dummy2, dummy2.next
        while pt is not None:
            next = pt.next
            pt.next = prev
            prev, pt = pt, next

        end2 = prev

        sumhead = ListNode()
        pt = sumhead
        carry_over = 0
        while not (end1 is dummy1 and end2 is dummy2) or carry_over:

            digitsum = carry_over
            if end1 is not dummy1:
                digitsum += end1.val
                end1 = end1.next
            if end2 is not dummy2:
                digitsum += end2.val
                end2 = end2.next

            if digitsum >= 10:
                carry_over = 1
                digitsum -= 10
            else:
                carry_over = 0

            pt.next = ListNode(val=digitsum)
            pt = pt.next

        prev, pt = sumhead, sumhead.next
        while pt is not None:
            next = pt.next
            pt.next = prev
            prev, pt = pt, next

        sumhead.next.next = None
        return prev

