# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        current = head
        carry_forward = 0
        while l1 is not None and l2 is not None:
            n = ListNode((l1.val + l2.val + carry_forward) % 10)
            carry_forward = (l1.val + l2.val + carry_forward) // 10
            current.next = n
            current = n
            l1, l2 = l1.next, l2.next
        if l1 is not None:
            current.next = l1
        elif l2 is not None:
            current.next = l2
        while carry_forward and current.next is not None:
            current = current.next
            carry_forward, current.val = (current.val + carry_forward) // 10, (current.val + carry_forward) % 10
        if carry_forward:
            current.next = ListNode(carry_forward)
        return head.next

# Runtime: 60 ms, faster than 96.65% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 14.1 MB, less than 85.40% of Python3 online submissions for Add Two Numbers.

# Time: O(n+m)
# Space: O(n+m)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_root = ListNode(-1)
        p = dummy_root
        prev_adder = 0
        while not( l1 is None and l2 is None) or prev_adder:
            if l1 is None:
                v1 = 0
            else:
                v1 = l1.val
                l1 = l1.next
            if l2 is None:
                v2 = 0
            else:
                v2 = l2.val
                l2 = l2.next
            nroot = ListNode((v1 + v2 + prev_adder) % 10 )
            prev_adder = (v1 + v2 + prev_adder) // 10
            p.next = nroot
            p = nroot
        return dummy_root.next


# Time Complexity: O(m + n), m for length of l1 and n for length of l2
# Space Complexity: O(m) or O(n) for whichever m or n is larger

# Runtime: 64 ms, faster than 90.37% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Add Two Numbers.