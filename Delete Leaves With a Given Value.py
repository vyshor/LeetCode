# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        parents = {}
        dummy = TreeNode(left=root)

        def explore(node):
            nonlocal parents
            if node.left is None and node.right is None and node.val == target:
                parent, is_left = parents[id(node)]
                if is_left:
                    parent.left = None
                else:
                    parent.right = None
                del parents[id(node)]
                explore(parent)

            if node.left is not None:
                parents[id(node.left)] = node, True
                explore(node.left)

            if node.right is not None:
                parents[id(node.right)] = node, False
                explore(node.right)

        explore(dummy)
        return dummy.left
