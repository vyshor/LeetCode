# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def prune(node):

            if node.left is not None:
                node.left = prune(node.left)

            if node.right is not None:
                node.right = prune(node.right)

            if node.left is None and node.right is None:
                return None if node.val == 0 else node

            return node

        return prune(root)
