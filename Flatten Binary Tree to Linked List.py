# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        def shiftLeftChild(node):
            if node is None:
                return

            if node.left is None and node.right is None:
                return

            if node.left is not None:
                shiftLeftChild(node.left)

            if node.right is not None:
                shiftLeftChild(node.right)

            if node.left is not None:
                node_right = node.right
                node.right, node.left = node.left, None

                pt = node.right
                while pt.right is not None:
                    pt = pt.right

                pt.right = node_right

        shiftLeftChild(root)