# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(next=head)
        prev = dummy_head
        pt = head
        s_pt = None
        while pt != None and pt.next != None:
            s_pt = pt.next
            prev.next, pt.next, s_pt.next = s_pt, s_pt.next, pt
            pt, prev = pt.next, pt
        return dummy_head.next

# Time: O(n)
# Space: O(1)

# Runtime: 32 ms, faster than 61.99% of Python3 online submissions for Swap Nodes in Pairs.
# Memory Usage: 14.2 MB, less than 53.15% of Python3 online submissions for Swap Nodes in Pairs.