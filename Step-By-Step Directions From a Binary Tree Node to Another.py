# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        path = []
        start_path = ''
        dest_path = ''

        def explore(node):
            nonlocal path, startValue, destValue, start_path, dest_path
            if node is None:
                return

            if node.val == startValue:
                start_path = ''.join(path)

            if node.val == destValue:
                dest_path = ''.join(path)

            path.append('L')
            explore(node.left)
            path.pop()

            path.append('R')
            explore(node.right)
            path.pop()

        explore(root)
        n1 = min(len(start_path), len(dest_path))
        i = 0
        while i < n1:
            if start_path[i] == dest_path[i]:
                i += 1
            else:
                break

        final_path = 'U' * (len(start_path) - i) + dest_path[i:]
        return final_path
