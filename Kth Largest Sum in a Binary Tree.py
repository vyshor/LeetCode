# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        summ = []

        def recur(node, level):
            nonlocal summ
            if not node:
                return

            if len(summ) == level:
                summ.append(node.val)
            else:
                summ[level] += node.val
            recur(node.left, level + 1)
            recur(node.right, level + 1)

        recur(root, 0)
        if len(summ) < k:
            return -1
        summ.sort()
        return summ[-k]
