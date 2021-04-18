# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummyHead = ListNode(next=head)
        before_start = dummyHead
        start = head
        end = before_start
        for _ in range(n):
            end = end.next
        while end.next:
            end = end.next
            before_start, start = start, start.next
        before_start.next = start.next
        return dummyHead.next

# Time: O(1)
# Space: O(1)

# Runtime: 32 ms, faster than 74.43% of Python3 online submissions for Remove Nth Node From End of List.
# Memory Usage: 14.2 MB, less than 77.52% of Python3 online submissions for Remove Nth Node From End of List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 1 2 (1)
# 1

# 1 (1)
# None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_head = ListNode(-1)
        dummy_head.next = head
        curr = dummy_head
        while curr:
            i = n
            pter = curr
            # Check if this is the node to be removed
            while i > 0:
                i -= 1
                pter = pter.next
            if not pter.next:
                # Found node to remove
                curr.next = curr.next.next
                return dummy_head.next
            else:
                curr = curr.next

# Time: O(n*k)
# Space: O(1)
# Runtime: 44 ms, faster than 22.00% of Python3 online submissions for Remove Nth Node From End of List.
# Memory Usage: 13.8 MB, less than 6.06% of Python3 online submissions for Remove Nth Node From End of List.

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_head = ListNode(-1)
        dummy_head.next = head
        curr = dummy_head
        pter = curr

        i = n
        while i > 0:
            i -= 1
            pter = pter.next

        while pter.next and curr:
            pter = pter.next
            curr = curr.next
        else:
            curr.next = curr.next.next
            return dummy_head.next

# Time: O(n)
# Space: O(1)
# Runtime: 36 ms, faster than 87.41% of Python3 online submissions for Remove Nth Node From End of List.
# Memory Usage: 13.7 MB, less than 6.06% of Python3 online submissions for Remove Nth Node From End of List.