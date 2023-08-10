# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        oddDummy = ListNode()
        evenDummy = ListNode()
        pt, odd, even = head, oddDummy, evenDummy
        while pt is not None:
            next = pt.next
            odd.next = pt
            odd = odd.next
            if next is None:
                break
            pt.next = None
            pt = next

            next = pt.next
            even.next = pt
            even = even.next
            if next is None:
                break
            pt.next = None
            pt = next

        odd.next = evenDummy.next
        return oddDummy.next


