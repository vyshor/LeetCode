# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        summ = []

        def addSum(node, level):
            if node is None:
                return

            if level >= len(summ):
                summ.append(node.val)
            else:
                summ[level] += node.val

            addSum(node.left, level + 1)
            addSum(node.right, level + 1)

        addSum(root, 0)
        maxx = max(summ)
        return summ.index(maxx) + 1
