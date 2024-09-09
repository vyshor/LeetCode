# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]
        i, j = 0, -1
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direct = 0
        ptr = head
        delta_x, delta_y = dirs[direct]
        while ptr:
            if i + delta_x < 0 or i + delta_x >= m or j + delta_y < 0 or j + delta_y >= n or matrix[i + delta_x][
                j + delta_y] != -1:
                direct += 1
                direct %= 4

                delta_x, delta_y = dirs[direct]

            i += delta_x
            j += delta_y
            matrix[i][j] = ptr.val
            ptr = ptr.next
        return matrix
