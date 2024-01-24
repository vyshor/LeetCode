# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        count = 0

        def checkNode(node, total, odd, even):
            nonlocal count
            if node is None:
                return

            total += 1
            val = node.val
            if val not in odd and val not in even:
                odd.add(val)
            elif val in odd:
                even.add(val)
                odd.remove(val)
            else:
                even.remove(val)
                odd.add(val)

            if node.left is None and node.right is None:
                count += (len(odd) == (total % 2 == 1))
                return

            checkNode(node.left, total, set(odd), set(even))
            checkNode(node.right, total, set(odd), set(even))

        checkNode(root, 0, set(), set())

        return count
