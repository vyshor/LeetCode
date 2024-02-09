# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        dp = []
        ans = []

        pt = head
        i = 0
        while pt is not None:
            while dp and pt.val > dp[-1][0]:
                _, idx = dp.pop()
                ans[idx] = pt.val

            ans.append(0)
            dp.append((pt.val, i))
            pt = pt.next
            i += 1
        return ans
