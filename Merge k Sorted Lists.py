# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def lt(self, other):
    return self.val < other.val

setattr(ListNode,'__lt__', lt)

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy_head = ListNode()
        pt = dummy_head
        h = [node for node in lists if node]
        heapq.heapify(h)
        while len(h):
            pt.next = heapq.heappop(h)
            pt = pt.next
            if pt.next:
                heapq.heappush(h, pt.next)
        return dummy_head.next

# Runtime: 104 ms, faster than 68.08% of Python3 online submissions for Merge k Sorted Lists.
# Memory Usage: 17.9 MB, less than 66.91% of Python3 online submissions for Merge k Sorted Lists.

# Time: O(n lgn), n being all the elements, lgn for heappush lgn for heappop
# Space: O(1)


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lst = []
        for l in lists:
            pt = l
            while pt:
                lst.append(pt.val)
                pt = pt.next
        lst.sort()
        dummy_head = ListNode(-1)
        pt = dummy_head
        for i in lst:
            pt.next = ListNode(i)
            pt = pt.next
        return dummy_head.next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lst = []
        for ll in lists:
            while ll != None:
                lst.append(ll.val)
                ll = ll.next
        lst.sort()
        root = ListNode(-1)
        prev = root
        for node in lst:
            # Probably wrong method, because you are supposed to just deal with pointers
            # Time: O(nlgn)
            # Space: O(n)
            # Runtime: 108 ms, faster than 87.84% of Python3 online submissions for Merge k Sorted Lists.
            # Memory Usage: 17.9 MB, less than 10.60% of Python3 online submissions for Merge k Sorted Lists.

            # Definition for singly-linked list.
            # class ListNode:
            #     def __init__(self, x):
            #         self.val = x
            #         self.next = None
            nexn = ListNode(node)
            prev.next = nexn
            prev = nexn
        return root.next


# Time: O(nlgn)
# Space: O(n)

# Runtime: 88 ms, faster than 99.69% of Python3 online submissions for Merge k Sorted Lists.
# Memory Usage: 16.6 MB, less than 45.45% of Python3 online submissions for Merge k Sorted Lists.
