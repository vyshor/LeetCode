# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        max_depth, val = 0, root.val

        def exploreNode(node, depth):
            nonlocal max_depth, val
            if node is None:
                return

            if depth > max_depth:
                max_depth = depth
                val = node.val

            exploreNode(node.left, depth + 1)
            exploreNode(node.right, depth + 1)

        exploreNode(root, 0)
        return val
