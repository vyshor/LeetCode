# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def compare(node1, node2):
            if node1 is None and node2 is None:
                return True

            if node1 is None or node2 is None:
                return False

            if node1.val != node2.val:
                return False

            left_nodes = [node1.left, node1.right]
            if node1.right is None or (node1.left is not None and node1.right.val < node1.left.val):
                left_nodes[0], left_nodes[1] = left_nodes[1], left_nodes[0]
            right_nodes = [node2.left, node2.right]
            if node2.right is None or (node2.left is not None and node2.right.val < node2.left.val):
                right_nodes[0], right_nodes[1] = right_nodes[1], right_nodes[0]

            return compare(left_nodes[0], right_nodes[0]) and compare(left_nodes[1], right_nodes[1])

        return compare(root1, root2)
