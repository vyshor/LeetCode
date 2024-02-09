# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums = set(nums)
        pt = head

        count = 0
        component = False
        while pt is not None:
            if pt.val in nums:
                component = True
            elif component:
                count += 1
                component = False
            pt = pt.next

        if component:
            count += 1

        return count

