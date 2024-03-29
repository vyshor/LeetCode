# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        b -= a
        b += 2

        pt = list1
        while a > 1:
            pt = pt.next
            a -= 1

        pt2 = pt
        while b > 0:
            pt2 = pt2.next
            b -= 1

        pt.next = list2
        while pt.next is not None:
            pt = pt.next

        pt.next = pt2
        return list1

# class Solution:
#     def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
#         dummyHead = ListNode(next=list1)
#         prev, pt = dummyHead, list1
#         for _ in range(a):
#             prev, pt = pt, pt.next
#
#         prev.next = list2
#         for _ in range(b - a + 1):
#             pt = pt.next
#
#         list2pt = list2
#         while list2pt.next is not None:
#             list2pt = list2pt.next
#
#         list2pt.next = pt
#         return dummyHead.next
