# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def sameTree(left, right):
            if left == right == None:
                return True

            if left is None or right is None:
                return False

            if left.val != right.val:
                return False

            return sameTree(left.left, right.left) and sameTree(left.right, right.right)

        return sameTree(p, q)

# class Solution:
#     def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
#         if not p and not q:
#             return True
#         else:
#             try:
#                 return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
#             except AttributeError:
#                 return False


# Time: O(n)  # Exactly visit each node once
# Space: O(n) for a long-chain tree
# Runtime: 36 ms, faster than 74.14% of Python3 online submissions for Same Tree.
# Memory Usage: 14 MB, less than 5.72% of Python3 online submissions for Same Tree.
