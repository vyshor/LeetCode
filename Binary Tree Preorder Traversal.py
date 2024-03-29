# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        ans = []
        q = [root]

        while q:
            node = q.pop()
            ans.append(node.val)
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)

        return ans
#
# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if root is None:
#             return []
#
#         ans = []
#
#         def printNode(node):
#             nonlocal ans
#             ans.append(node.val)
#             if node.left:
#                 printNode(node.left)
#             if node.right:
#                 printNode(node.right)
#
#         printNode(root)
#         return ans
