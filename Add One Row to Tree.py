# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val=val, left=root)

        def exploreNode(node, d):
            if node is None:
                return

            if d == 1:
                node.left = TreeNode(val=val, left=node.left)
                node.right = TreeNode(val=val, right=node.right)

            exploreNode(node.left, d - 1)
            exploreNode(node.right, d - 1)

        exploreNode(root, depth - 1)
        return root

# class Solution:
#     def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
#         dummy = TreeNode(left=root)
#         def addNode(node, cd):
#             if not node or cd < 1:
#                 return
#             if cd == 2:
#                 node.left = TreeNode(val=v, left=node.left)
#                 node.right = TreeNode(val=v, right=node.right)
#                 return
#             addNode(node.left, cd-1)
#             addNode(node.right, cd-1)
#         addNode(dummy, d+1)
#         return dummy.left
#
# # Time: O(n)
# # Space: O(1)
#
# # Runtime: 52 ms, faster than 82.23% of Python3 online submissions for Add One Row to Tree.
# # Memory Usage: 17.3 MB, less than 24.93% of Python3 online submissions for Add One Row to Tree.
