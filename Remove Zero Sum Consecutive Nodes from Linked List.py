# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dp = collections.OrderedDict()
        dummyHead = ListNode(next=head)
        pt = dummyHead
        summ = 0
        while pt is not None:
            summ += pt.val
            if summ in dp:
                old_pt = dp[summ]
                old_pt.next = pt.next

                while summ in dp:
                    dp.popitem()

                dp[summ] = old_pt
            else:
                dp[summ] = pt

            pt = pt.next

        return dummyHead.next
