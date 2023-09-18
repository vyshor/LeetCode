# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        dp = set()
        ans_visited = set()
        ans = []

        def exploreNode(node):
            if node.left is None and node.right is None:
                path = (node.val,)
                if path in dp and path not in ans_visited:
                    ans.append(node)
                    ans_visited.add(path)
                dp.add(path)
                return path

            leftPath = ()
            if node.left is not None:
                leftPath = exploreNode(node.left)

            rightPath = ()
            if node.right is not None:
                rightPath = exploreNode(node.right)

            path = (leftPath, rightPath, node.val)
            if path in dp and path not in ans_visited:
                ans.append(node)
                ans_visited.add(path)

            dp.add(path)

            return path

        exploreNode(root)
        return ans
