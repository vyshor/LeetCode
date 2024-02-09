# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        def exploreNode(node, currentSum):
            if node.left is None and node.right is None:
                return currentSum + node.val == targetSum

            currentSum += node.val
            if node.left is not None:
                left = exploreNode(node.left, currentSum)
                if left:
                    return True

            if node.right is not None:
                right = exploreNode(node.right, currentSum)
                if right:
                    return True

            return False

        return exploreNode(root, 0)
