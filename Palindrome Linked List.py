# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True

        fast, slow = head.next, head
        while fast is not None:
            fast = fast.next
            slow = slow.next

            if fast is None:
                break
            fast = fast.next

        pt, prev = slow.next, slow
        while pt is not None:
            next = pt.next
            pt.next = prev
            prev, pt = pt, next

        while head is not slow:
            if head.val != prev.val:
                return False
            else:
                head = head.next
                prev = prev.next
        return True
