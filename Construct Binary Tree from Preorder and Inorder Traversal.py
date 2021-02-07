# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# preorder
# mid left right
# inorder
# left mid right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def buildNode(preorder, inorder):
            if not preorder:
                return None
            mid = preorder[0]
            mid_idx = inorder.index(mid)
            rootNode = TreeNode(mid)
            rootNode.left = buildNode(preorder[1:mid_idx + 1], inorder[:mid_idx])
            rootNode.right = buildNode(preorder[mid_idx + 1:], inorder[mid_idx + 1:])
            return rootNode

        root = buildNode(preorder, inorder)
        return root

# Time: O(n*d) # D for depth of tree
# Space: O(n*d)
# Runtime: 204 ms, faster than 31.26% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
# Memory Usage: 89 MB, less than 5.26% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.