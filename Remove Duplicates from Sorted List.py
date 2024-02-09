# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dp = set()
        dummy = ListNode(next=head)
        pt, prev = head, dummy
        while pt is not None:
            if pt.val not in dp:
                dp.add(pt.val)
                prev.next = pt
                prev = pt
            pt = pt.next
        prev.next = None
        return dummy.next
