# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def sortLinkedList(headA):
            if headA is None or headA.next is None:
                return headA

            dummy = ListNode(next=headA)
            slow, fast = headA, headA.next
            while fast.next is not None:
                fast = fast.next
                slow = slow.next

                if fast.next is None:
                    break
                fast = fast.next

            left, right = dummy.next, slow.next
            slow.next, fast.next = None, None
            left, right = sortLinkedList(left), sortLinkedList(right)
            return mergeList(left, right)

        def mergeList(headA, headB):
            dummy = ListNode()
            pt = dummy
            while headA is not None and headB is not None:
                if headA.val <= headB.val:
                    pt.next = headA
                    headA = headA.next
                else:
                    pt.next = headB
                    headB = headB.next
                pt = pt.next

            if headA is not None:
                pt.next = headA
            if headB is not None:
                pt.next = headB
            return dummy.next

        return sortLinkedList(head)

