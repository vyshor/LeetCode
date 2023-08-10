# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        fast, slow = head.next.next, head.next
        fast_count, slow_count = 2, 1

        if fast is None:
            return None

        while 1:
            if fast.next is None:
                return None

            if fast is slow:
                while slow is not head:
                    slow = slow.next
                    head = head.next
                return head
            else:
                if fast.next:
                    fast = fast.next
                    fast_count += 1

                if slow.next:
                    slow = slow.next
                    slow_count += 1

                if fast is slow:
                    continue

                if fast.next:
                    fast = fast.next
                    fast_count += 1



