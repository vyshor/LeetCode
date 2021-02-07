# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def findNode(root, path, targetId):
            if root is None:
                return None
            if id(root) == targetId:
                return path
            else:
                r = findNode(root.right, path + [1], targetId)
                if r:
                    return r
                l = findNode(root.left, path + [0], targetId)
                if l:
                    return l
                return None

        def seekNode(root, path):
            if not path:
                return root
            else:
                if path[0] == 0:
                    return seekNode(root.left, path[1:])
                else:
                    return seekNode(root.right, path[1:])

        nodePath = findNode(original, [], id(target))
        return seekNode(cloned, nodePath)


# Runtime: 680 ms, faster than 16.24% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.
# Memory Usage: 24.3 MB, less than 18.54% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.

# Time: O(V+E) for V, E being the verticies and edges of the tree
# Space: O(D) for D being the depth of the tree