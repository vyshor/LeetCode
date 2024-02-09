# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        dp = {}

        def ignoreNode(node, depth):
            if dp[node.val] < depth:
                dp[node.val] = depth

                if node.left is not None:
                    ignoreNode(node.left, depth)

                if node.right is not None:
                    ignoreNode(node.right, depth)

        def exploreNode(node, depth):
            dp[node.val] = depth

            depth += 1

            if node.left is None and node.right is None:
                return depth

            leftDepth, rightDepth = 0, 0

            if node.left is not None:
                leftDepth = exploreNode(node.left, depth)

            if node.right is not None:
                rightDepth = exploreNode(node.right, depth)

            if node.left is not None and node.right is not None:
                ignoreNode(node.left, rightDepth)
                ignoreNode(node.right, leftDepth)

            return max(rightDepth, leftDepth)

        exploreNode(root, -1)
        # print(dp)
        return [dp[query] for query in queries]
