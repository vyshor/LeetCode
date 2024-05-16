# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def explore(node):
            if node.left is None and node.right is None:
                return bool(node.val)

            elif node.val == 2:
                return explore(node.left) or explore(node.right)

            else:
                return explore(node.left) and explore(node.right)

        return explore(root)
