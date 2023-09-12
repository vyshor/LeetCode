# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findNodePath(node, val, path):
            path.append(node)

            if node.val == val:
                return path

            if node.left is not None:
                leftPath = findNodePath(node.left, val, path)
                if leftPath is not None:
                    return leftPath

            if node.right is not None:
                rightPath = findNodePath(node.right, val, path)
                if rightPath is not None:
                    return rightPath

            path.pop()
            return None

        pPath = findNodePath(root, p.val, [])
        qPath = findNodePath(root, q.val, [])

        pSet = set(pPath)

        # print(pPath)
        # print(qPath)

        for i in range(len(qPath) - 1, -1, -1):
            if qPath[i] in pSet:
                return qPath[i]

