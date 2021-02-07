# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# Time: O(n) # each node visited once
# Space: O(n) for long chained unbalanced tree
# Runtime: 44 ms, faster than 93.06% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 16.1 MB, less than 6.25% of Python3 online submissions for Maximum Depth of Binary Tree.