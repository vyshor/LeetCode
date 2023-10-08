# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def depth(node):
            if node is None:
                return float('inf')

            if node.left is None and node.right is None:
                return 1

            return min(depth(node.left), depth(node.right)) + 1

        return depth(root)
