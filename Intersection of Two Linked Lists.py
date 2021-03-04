# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = 0, 0
        p1, p2 = headA, headB
        while p1 is not None:
            a += 1
            p1 = p1.next
        while p2 is not None:
            b += 1
            p2 = p2.next
        p1, p2 = headA, headB
        if a > b:
            for _ in range(a - b):
                p1 = p1.next
        else:
            for _ in range(b - a):
                p2 = p2.next
        while p1 and p2:
            if p1 == p2:
                return p1
            else:
                p1 = p1.next
                p2 = p2.next
        return None

# Time: O(n+m)
# Space: O(1)

# Runtime: 160 ms, faster than 76.92% of Python3 online submissions for Intersection of Two Linked Lists.
# Memory Usage: 29.5 MB, less than 34.55% of Python3 online submissions for Intersection of Two Linked Lists.

