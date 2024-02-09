# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0

        def sumTree(node):
            nonlocal count
            if node is None:
                return 0, 0

            left_val, left_count = sumTree(node.left)
            right_val, right_count = sumTree(node.right)
            summ = node.val + left_val + right_val
            tree_counts = 1 + left_count + right_count

            if node.val == summ // tree_counts:
                count += 1

            return summ, tree_counts

        sumTree(root)
        return count
