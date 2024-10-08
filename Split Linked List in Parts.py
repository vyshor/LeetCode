# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        ptr = head
        while ptr:
            n += 1
            ptr = ptr.next
        m = n // k
        k2 = n % k
        ptr = head
        arr = []
        while ptr:
            arr.append(ptr)
            i = 0
            while i < (m - 1 + int(k2 > 0)) and ptr:
                ptr = ptr.next
                i += 1
            k2 -= 1
            if ptr:
                nxt = ptr.next
                ptr.next = None
                ptr = nxt
        while len(arr) < k:
            arr.append(None)
        return arr


# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
#         if head is None:
#             return [None] * k
#
#         if k == 1:
#             return [head]
#
#         pt = head
#         n = 0
#
#         while pt is not None:
#             n += 1
#             pt = pt.next
#
#         split = n // k
#         extra = n % k
#
#         pt = head
#         splits = [pt]
#
#         count = split
#         if extra:
#             count += 1
#             extra -= 1
#
#         while count > 0 and pt is not None:
#             count -= 1
#             prev, pt = pt, pt.next
#
#             if count == 0:
#                 prev.next = None
#                 if pt is None:
#                     break
#
#                 splits.append(pt)
#
#                 count = split
#                 if extra:
#                     count += 1
#                     extra -= 1
#
#         while len(splits) < k:
#             splits.append(None)
#
#         return splits




