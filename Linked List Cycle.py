# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        fast, slow = head.next, head
        while fast is not None:
            fast = fast.next
            slow = slow.next

            if fast == slow:
                return True

            if fast is not None:
                fast = fast.next

                if fast == slow:
                    return True

        return False


# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         if head is None or head.next is None:
#             return False
#
#         fast, slow = head.next, head
#         while fast is not None:
#             fast = fast.next
#             slow = slow.next
#
#             if fast == slow:
#                 return True
#
#             if fast is not None:
#                 fast = fast.next
#
#                 if fast == slow:
#                     return True
#
#         return False

# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         turtle = head
#         rabbit = head
#         while rabbit:
#             turtle = turtle.next
#             rabbit = rabbit.next
#             if not rabbit:
#                 return False
#             rabbit = rabbit.next
#             if rabbit and rabbit.val == turtle.val:
#                 return True
#         return False

# Runtime: 52 ms, faster than 44.73% of Python3 online submissions for Linked List Cycle.
# Memory Usage: 17.3 MB, less than 19.25% of Python3 online submissions for Linked List Cycle.
# Time: O(n)
# Space: O(1)

# class Solution(object):
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         dp = {}
#         cur = head
#         while cur:
#             try:
#                 dp[id(cur)] # Appeared before
#                 return True
#             except KeyError:
#                 dp[id(cur)] = True
#             cur = cur.next
#         return False

# Space: O(n)
# Time: O(n)
# Runtime: 48 ms, faster than 14.71% of Python online submissions for Linked List Cycle.
# Memory Usage: 19 MB, less than 11.35% of Python online submissions for Linked List Cycle.

# class Solution(object):
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         dp = []
#         cur = head
#         while cur:
#             if id(cur) in dp: # Appeared before
#                 return True
#             else:
#                 dp.append(id(cur))
#             cur = cur.next
#         return False

# Time: O(n^2)
# Space: O(n)
# Runtime: 1096 ms, faster than 5.38% of Python online submissions for Linked List Cycle.
# Memory Usage: 18.4 MB, less than 26.24% of Python online submissions for Linked List Cycle.

# class Solution(object):
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         if not head:
#             return False
#         turtle = head
#         rabbit = head.next
#         while rabbit:
#             rabbit = rabbit.next
#             if rabbit is turtle:
#                 return True
#             else:
#                 if not rabbit:
#                     return False
#                 rabbit = rabbit.next
#                 turtle = turtle.next
#                 if rabbit is turtle:
#                     return True
#         return False

# Time: O(n)
# Space: O(1)
# Runtime: 36 ms, faster than 81.04% of Python online submissions for Linked List Cycle.
# Memory Usage: 18.2 MB, less than 60.28% of Python online submissions for Linked List Cycle.