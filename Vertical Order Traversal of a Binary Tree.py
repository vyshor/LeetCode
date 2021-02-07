# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        dp = {}

        # Process nodes
        def processNode(node, pos):
            if not node:
                return
            x, y = pos
            if x in dp.keys():
                if y in dp[x].keys():
                    dp[x][y].append(node.val)
                else:
                    dp[x][y] = [node.val]
            else:
                dp[x] = {y: [node.val]}

            processNode(node.left, (x-1, y-1))
            processNode(node.right, (x+1, y-1))

        processNode(root, (0,0))

        ans = []
        # Construct list
        for x in sorted(list(dp.keys())):
            to_append = []
            for y in sorted(list(dp[x].keys()), reverse=True):
                if len(dp[x][y]) == 1:
                    to_append.append(dp[x][y][0])
                else:
                    to_append += sorted(dp[x][y])
            ans.append(to_append)
        return ans

# Runtime: 36 ms, faster than 54.10% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.
# Memory Usage: 14.6 MB, less than 65.37% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.

# Time: O(n)
# Space: O(n)