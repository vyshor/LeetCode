# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        right_view = []
        def processNode(node, level):
            if not node:
                return
            if len(right_view) > level:
                right_view[level] = node.val
            else:
                right_view.append(node.val)
            processNode(node.left, level+1)
            processNode(node.right, level+1)
        processNode(root, 0)
        return right_view

# Time: O(n)
# Space: O(n)
# Runtime: 36 ms, faster than 37.97% of Python3 online submissions for Binary Tree Right Side View.
# Memory Usage: 14.1 MB, less than 93.90% of Python3 online submissions for Binary Tree Right Side View.
