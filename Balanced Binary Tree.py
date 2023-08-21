# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balanced(node):
            if node is None:
                return True, -1

            left_d, right_d = 0, 0
            left, right = True, True

            if node.left is not None:
                left, left_d = balanced(node.left)
                if not left:
                    return left, 0

            if node.right is not None:
                right, right_d = balanced(node.right)
                if not right:
                    return right, 0

            depth = max(right_d, left_d) + 1
            return left and right and abs(right_d - left_d) <= 1, depth

        return balanced(root)[0]


