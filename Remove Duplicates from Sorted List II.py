# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        n = head
        dp = {}
        while (n != None):
            if not dp.get(n.val):
                dp[n.val] = 1
            else:
                dp[n.val] += 1
            n = n.next

        dummy_head = ListNode()
        dummy_head.next = None
        n = head
        prev = dummy_head

        while (n != None):
            if not (dp[n.val] > 1):
                prev.next = n
                prev = n
            n = n.next
            if n == None:
                prev.next = n
        return dummy_head.next


# Runtime: 44 ms, faster than 41.95% of Python3 online submissions for Remove Duplicates from Sorted List II.
# Memory Usage: 14.2 MB, less than 74.65% of Python3 online submissions for Remove Duplicates from Sorted List II.

# Time: O(n) for n being length of array
# Space: O(n)