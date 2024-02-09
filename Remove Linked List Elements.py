# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head

        dummy = ListNode(next=head)
        pt, prev = head, dummy
        while pt is not None:
            if pt.val == val:
                prev.next = pt.next
            else:
                prev = pt

            pt = pt.next
        return dummy.next