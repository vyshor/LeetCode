# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        else:
            try:
                return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            except AttributeError:
                return False


# Time: O(n)  # Exactly visit each node once
# Space: O(n) for a long-chain tree
# Runtime: 36 ms, faster than 74.14% of Python3 online submissions for Same Tree.
# Memory Usage: 14 MB, less than 5.72% of Python3 online submissions for Same Tree.