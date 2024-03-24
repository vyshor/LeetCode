# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next is None:
            return

            # Find midpoint
        slow, fast = head, head.next
        while fast.next is not None:
            fast = fast.next
            slow = slow.next

            if fast.next is None:
                break
            fast = fast.next

        pt = slow.next

        # Detach midpoint
        slow.next = None

        # Reverse second half
        n = pt.next
        pt.next = None
        while n is not None:
            n2 = n.next
            n.next = pt
            pt, n = n, n2

        pt1, pt2 = head, pt
        while pt1 is not None and pt2 is not None:
            pt3 = pt2.next
            pt2.next = pt1.next
            pt1.next = pt2
            pt1, pt2 = pt1.next.next, pt3


# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         """
#         Do not return anything, modify head in-place instead.
#         """
#         if head.next is None:
#             return
#
#         slow, fast = head, head.next
#         while fast.next is not None:
#             fast = fast.next
#             slow = slow.next
#
#             if fast.next is None:
#                 break
#             fast = fast.next
#
#         prev, pt = slow, slow.next
#         slow.next = None
#         while pt is not None:
#             next = pt.next
#             pt.next = prev
#             prev, pt = pt, next
#
#         start, end = head, prev
#         # print(head)
#         # print(end)
#         while start is not None:
#             next = start.next
#             start.next = end
#             next_end = end.next
#             end.next = next
#
#             start, end = next, next_end
#
