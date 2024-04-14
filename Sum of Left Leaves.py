# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        summ = 0
        def exploreNode(node, left_node):
            nonlocal summ
            if node is None:
                return
            if node.left is None and node.right is None and left_node:
                summ += node.val
            exploreNode(node.left, True)
            exploreNode(node.right, False)
        exploreNode(root, False)
        return summ
