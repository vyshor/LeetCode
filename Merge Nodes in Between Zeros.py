# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head.next
        new_ptr = head
        summ = 0
        while ptr is not None:
            while ptr.val != 0:
                summ += ptr.val
                ptr = ptr.next

            new_ptr.val = summ
            summ = 0
            ptr = ptr.next
            if ptr is None:
                new_ptr.next = None
            else:
                new_ptr = new_ptr.next

        new_ptr.next = None
        return head
