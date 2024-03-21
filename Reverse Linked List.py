# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        pt1, pt2 = head, head.next
        pt1.next = None

        while pt2 is not None:
            pt3 = pt2.next
            pt2.next = pt1
            pt1, pt2 = pt2, pt3

        return pt1
#
#
# import unittest
#
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         # stack = []
#         # dummy = ListNode(-1)
#         # dummy.next = head
#         # cur = dummy.next
#         # while cur:
#         #     stack.append(cur)
#         #     prev = cur
#         #     cur = cur.next
#         #     prev.next = None
#         # cur = dummy
#         # while stack:
#         #     cur.next = stack.pop()
#         #     cur = cur.next
#         # return dummy.next
#
# # Time: O(n)
# # Space: O(n)
# # Runtime: 48 ms, faster than 19.74% of Python3 online submissions for Reverse Linked List.
# # Memory Usage: 15 MB, less than 31.82% of Python3 online submissions for Reverse Linked List.
#
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         cur = head
#         prev = None
#         while cur:
#             next = cur.next
#             cur.next = prev
#
#             prev = cur
#             cur = next
#         return prev
#
# # Time: O(n)
# # Space: O(1)
# # Runtime: 40 ms, faster than 83.06% of Python3 online submissions for Reverse Linked List.
# # Memory Usage: 14.9 MB, less than 31.82% of Python3 online submissions for Reverse Linked List.
#
# class TestSolution(unittest.TestCase):
#     def testA(self):
#         n1 = ListNode(1)
#         n2 = ListNode(2)
#         n3 = ListNode(3)
#         head = n1
#         n1.next = n2
#         n2.next = n3
#
#         cur = head
#         pre_result = []
#         while cur:
#             pre_result.append(cur.val)
#             cur = head.next
#
#         result = Solution().reverseList(head)
#
#         cur = result
#         post_result = []
#         while cur:
#             pre_result.append(cur.val)
#             cur = head.next
#         self.assertEqual(pre_result, reversed(post_result))
