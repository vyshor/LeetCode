# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def exploreNode(node, path):
            if node is None:
                return path

            path.appendleft(node.val)
            if node.left and node.right:
                left_path = exploreNode(node.left, deque(path))
                right_path = exploreNode(node.right, deque(path))
                return min(left_path, right_path)
            elif node.left:
                return exploreNode(node.left, path)
            elif node.right:
                return exploreNode(node.right, path)
            else:
                return path

        arr = exploreNode(root, deque([]))
        n = len(arr)
        ans = []
        for i in range(n):
            if arr[i] >= 0:
                ans.append(chr(arr[i] + 97))
        return ''.join(ans)
