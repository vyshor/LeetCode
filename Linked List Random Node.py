# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.dp = []
        pt = head
        while pt is not None:
            self.dp.append(pt.val)
            pt = pt.next
        self.size = len(self.dp)

    def getRandom(self) -> int:
        return self.dp[random.randint(0, self.size-1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
