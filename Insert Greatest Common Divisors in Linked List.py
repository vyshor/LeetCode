# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            if b == 0:
                return a

            return gcd(b, a % b)

        prev, cur = None, head
        pval, cval = 0, head.val
        while cur.next:
            prev, cur = cur, cur.next
            pval, cval = cval, cur.val
            prev.next = ListNode(val=gcd(pval, cval), next=cur)
        return head
