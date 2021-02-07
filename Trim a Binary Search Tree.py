# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def trimNode(node, low, high):
            if not node:
                return

            node.left = trimNode(node.left, low, high)
            node.right = trimNode(node.right, low, high)

            desc = node.left
            if not desc:
                desc = node.right
            if node.val < low or node.val > high:
                return desc
            return node

        return trimNode(root, low, high)


# Runtime: 100 ms, faster than 5.30% of Python3 online submissions for Trim a Binary Search Tree.
# Memory Usage: 16.5 MB, less than 92.64% of Python3 online submissions for Trim a Binary Search Tree.
# Time: O(N)
# Space: O(N)