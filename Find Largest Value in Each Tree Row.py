# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        dp = []

        def updateNode(node, depth):
            if node is None:
                return

            if depth < len(dp):
                dp[depth] = max(dp[depth], node.val)
            else:
                dp.append(node.val)

            updateNode(node.left, depth + 1)
            updateNode(node.right, depth + 1)

        updateNode(root, 0)
        return dp
