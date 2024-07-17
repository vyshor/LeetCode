# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        nodes = []
        to_delete = set(to_delete)
        dummy = TreeNode(left=root)

        def explore(node, parent, is_left):
            nonlocal nodes
            if node is None:
                return

            explore(node.left, node, True)
            explore(node.right, node, False)

            if node.val in to_delete:
                if is_left:
                    parent.left = None
                else:
                    parent.right = None

                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)

        explore(root, dummy, True)
        if dummy.left:
            nodes.append(dummy.left)
        return nodes
