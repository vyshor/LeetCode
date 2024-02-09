# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def getDepthAndDiameter(node):
            if node is None:
                return 0, 0

            leftDepth, leftDiameter = 0, 0
            if node.left is not None:
                leftDepth, leftDiameter = getDepthAndDiameter(node.left)
                leftDepth += 1

            rightDepth, rightDiameter = 0, 0
            if node.right is not None:
                rightDepth, rightDiameter = getDepthAndDiameter(node.right)
                rightDepth += 1

            currentDiameter = max(leftDepth + rightDepth, leftDiameter, rightDiameter)
            currentDepth = max(leftDepth, rightDepth)

            return currentDepth, currentDiameter

        return getDepthAndDiameter(root)[1]
