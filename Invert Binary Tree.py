# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

# Time: O(n)
# Space: O(n)
# Runtime: 40 ms, faster than 38.79% of Python3 online submissions for Invert Binary Tree.
# Memory Usage: 13.7 MB, less than 5.41% of Python3 online submissions for Invert Binary Tree.