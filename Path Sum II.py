# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []

        ans = []

        def exploreNode(node, path, summ):
            path.append(node.val)
            summ += node.val

            # Node is leaf
            if node.left is None and node.right is None:
                if summ == targetSum:
                    ans.append(tuple(path))

            else:
                if node.left is not None:
                    exploreNode(node.left, path, summ)
                if node.right is not None:
                    exploreNode(node.right, path, summ)

            summ -= path.pop()

        exploreNode(root, [], 0)
        return ans

