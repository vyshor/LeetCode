# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        minn, maxx = float('inf'), 0
        first_idx = -1
        prev_idx = -1

        i = 1
        ptr, prev = head.next, head
        while ptr.next:
            critical = (prev.val < ptr.val and ptr.val > ptr.next.val) or (
                        prev.val > ptr.val and ptr.val < ptr.next.val)
            if critical:
                if first_idx == -1:
                    first_idx = i

                if prev_idx != -1:
                    minn = min(minn, i - prev_idx)
                    maxx = max(maxx, i - first_idx)
                prev_idx = i

            prev, ptr = ptr, ptr.next
            i += 1

        if prev_idx == first_idx:
            return [-1, -1]
        return [minn, maxx]
