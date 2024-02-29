# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        levels = []

        def exploreNode(node, depth):
            nonlocal levels
            if node is None:
                return True

            if len(levels) == depth:
                levels.append([])

            if len(levels[depth]) > 0:
                last_num = levels[depth][-1]
                if depth & 1:  # Odd level
                    if last_num <= node.val:  # Not decreasing
                        return False
                else:
                    if last_num >= node.val:  # Not increasing
                        return False

            if depth & 1:  # Odd level
                if node.val & 1:  # Odd number
                    return False
            else:  # Even level
                if node.val & 1 == 0:  # Even number
                    return False

            levels[depth].append(node.val)
            return exploreNode(node.left, depth + 1) and exploreNode(node.right, depth + 1)

        return exploreNode(root, 0)
