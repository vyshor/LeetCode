# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.resolveNode(root)

    def next(self) -> int:
        node = self.stack.pop()
        if node.right is not None:
            self.resolveNode(node.right)

        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) != 0

    def resolveNode(self, node):
        self.stack.append(node)
        if node.left is not None:
            self.resolveNode(node.left)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
