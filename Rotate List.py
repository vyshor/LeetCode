# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0:
            return head

        if head is None:
            return head

        pt = head
        n = 1
        while pt.next is not None:
            n += 1
            pt = pt.next
        pt.next = head

        k = n - (k % n)

        pt = head
        new_head = pt
        while k > 0:
            k -= 1
            if k == 0:
                new_head = pt.next
                pt.next = None
                pt = new_head
            else:
                pt = pt.next

        return new_head
