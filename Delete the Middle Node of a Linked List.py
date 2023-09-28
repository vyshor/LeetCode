# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None

        dummyHead = ListNode(next=head)
        prev, slow, fast = dummyHead, head, head.next

        while fast is not None:
            fast = fast.next
            prev, slow = slow, slow.next

            if fast is not None:
                fast = fast.next

        prev.next = slow.next

        return dummyHead.next
