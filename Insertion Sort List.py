# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        def addToList(dummy_head, node):
            prev, pt = dummy_head, dummy_head.next
            while pt is not None and node.val >= pt.val:
                pt, prev = pt.next, pt
            prev.next, node.next = node, pt

        dummy = ListNode(next=None)
        pt = head
        while pt is not None:
            next = pt.next
            addToList(dummy, pt)
            pt = next

        return dummy.next

