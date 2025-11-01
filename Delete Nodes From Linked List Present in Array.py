# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        dummy = ListNode(next=head)
        prev, ptr = dummy, head

        while ptr:
            if ptr.val in nums:
                prev.next = ptr.next
                ptr = ptr.next
            else:
                prev, ptr = ptr, ptr.next
        return dummy.next