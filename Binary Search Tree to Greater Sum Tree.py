# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def check(node, summ):
            if node is None:
                return summ

            summ = check(node.right, summ)
            summ += node.val
            node.val = summ
            return check(node.left, summ)

        check(root, 0)
        return root

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def bstToGst(self, root: TreeNode) -> TreeNode:
#         def processNode(node, rightsum):
#             if not node:
#                 return rightsum
#             rightsum = processNode(node.right, rightsum)
#             rightsum += node.val
#             node.val = rightsum
#             return processNode(node.left, rightsum)
#         processNode(root, 0)
#         return root
#
# # Runtime: 28 ms, faster than 86.15% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
# # Memory Usage: 14.3 MB, less than 33.99% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
#
# # Time: O(1)
# # Space: O(1)