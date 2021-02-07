# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        n1 = l1
        n2 = l2
        cn = dummy
        dummy.next = cn

        while (n1 != None and n2 != None):
            if n1.val < n2.val:
                cn.next = n1
                cn = cn.next
                n1 = n1.next
            else:
                cn.next = n2
                cn = cn.next
                n2 = n2.next

        if n2 != None:
            cn.next = n2
        else:
            cn.next = n1

        return dummy.next

# Runtime: 40 ms, faster than 44.11% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 14.2 MB, less than 75.61% of Python3 online submissions for Merge Two Sorted Lists.

# Time: O(n+m) , n, m being the size of the array
# Space: O(1)