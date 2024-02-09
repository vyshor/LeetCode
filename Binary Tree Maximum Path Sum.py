# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = root.val

        def maxNode(node):
            nonlocal ans
            ans = max(ans, node.val)

            if node.left is None and node.right is None:
                return node.val

            maxLeft = 0
            if node.left is not None:
                maxLeft = maxNode(node.left)

            maxRight = 0
            if node.right is not None:
                maxRight = maxNode(node.right)

            ans = max(ans, maxLeft + node.val + maxRight, maxLeft + node.val, maxRight + node.val)

            return max(maxLeft + node.val, maxRight + node.val, node.val)

        maxNode(root)
        return ans
