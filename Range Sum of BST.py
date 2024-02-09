# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def readNode(node):
            if node is None:
                return 0

            summ = 0
            if low <= node.val <= high:
                summ = node.val

            if not node.val > high:
                summ += readNode(node.right)

            if not node.val < low:
                summ += readNode(node.left)

            return summ

        return readNode(root)
