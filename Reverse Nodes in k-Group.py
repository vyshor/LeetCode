# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head.next is None or k == 1:
            return head

        dummyHead = ListNode(next=head)
        prev, pt = dummyHead, dummyHead.next

        while pt.next is not None:
            recee = pt
            count = 1
            while recee.next is not None and count < k:
                recee = recee.next
                count += 1

            if count < k:
                break

            subnext = recee.next
            subhead, subtail = prev, pt
            pt, prev = pt.next, pt

            while pt is not subnext:
                next = pt.next
                pt.next = prev
                prev, pt = pt, next
            subhead.next, subtail.next = prev, subnext

            if subnext is None:
                break

            prev, pt = subtail, subnext
        return dummyHead.next
