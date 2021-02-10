# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def processNode(node, rightsum):
            if not node:
                return rightsum
            rightsum = processNode(node.right, rightsum)
            rightsum += node.val
            node.val = rightsum
            return processNode(node.left, rightsum)
        processNode(root, 0)
        return root

# Time: O(n)
# Space: O(n)

# Runtime: 84 ms, faster than 58.69% of Python3 online submissions for Convert BST to Greater Tree.
# Memory Usage: 16.7 MB, less than 50.21% of Python3 online submissions for Convert BST to Greater Tree.