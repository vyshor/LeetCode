# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head.next is None:
            return head

        slow, fast = head, head.next
        total_count = 2
        oddLen = False

        while fast.next is not None:
            fast = fast.next
            slow = slow.next
            total_count += 2

            if fast.next is None:
                total_count -= 1
                break

            fast = fast.next

        first = head
        for _ in range(k - 1):
            first = first.next

        latter = head
        for _ in range(total_count - k):
            latter = latter.next

        first.val, latter.val = latter.val, first.val
        return head
