# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def explore(node):
            nett = node.val - 1
            cost = 0
            if node.left:
                left_nett, left_cost = explore(node.left)
                cost += left_cost + abs(left_nett)
                nett += left_nett

            if node.right:
                right_nett, right_cost = explore(node.right)
                cost += right_cost + abs(right_nett)
                nett += right_nett

            return nett, cost

        return explore(root)[1]
