# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        dp = {}
        dp_incoming = {}
        for desc in descriptions:
            p, c, l = desc
            if c not in dp_incoming:
                dp_incoming[c] = 1
            else:
                dp_incoming[c] += 1

            if p not in dp_incoming:
                dp_incoming[p] = 0

            if p not in dp:
                dp[p] = TreeNode(val=p)

            if c not in dp:
                dp[c] = TreeNode(val=c)

            if l:
                dp[p].left = dp[c]
            else:
                dp[p].right = dp[c]

        for k, v in dp_incoming.items():
            if v == 0:
                return dp[k]

