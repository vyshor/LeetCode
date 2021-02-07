# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def processNode(node, prefix):
            if node != None:
                if not node.left and not node.right:
                    return int(prefix + str(node.val))
                else:
                    prefix += str(node.val)
                    left_val = processNode(node.left, prefix)
                    right_val = processNode(node.right, prefix)
                    return left_val + right_val
            else:
                return 0

        return processNode(root, '')

# Runtime: 36 ms, faster than 53.56% of Python3 online submissions for Sum Root to Leaf Numbers.
# Memory Usage: 13.9 MB, less than 74.17% of Python3 online submissions for Sum Root to Leaf Numbers.
# Time: O(n)
# Space: O(n)
