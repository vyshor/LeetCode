# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head.next
        if fast is None:
            return slow

        while fast is not None:
            fast = fast.next
            slow = slow.next

            if fast is None:
                return slow

            fast = fast.next

        return slow

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head.next is None:
#             return head
#
#         slow, fast = head, head.next
#         oddCount = False
#         while fast.next is not None:
#             fast = fast.next
#             slow = slow.next
#
#             if fast.next is None:
#                 oddCount = True
#                 break
#             fast = fast.next
#
#         if not oddCount:
#             slow = slow.next
#
#         return slow
