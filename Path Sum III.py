# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0

        ans = 0

        def exploreNode(node, counter):
            nonlocal ans
            if node.val == targetSum:
                ans += 1

            seek = targetSum - node.val
            if seek in counter:
                ans += counter[seek]

            new_counter = {}
            for val, count in counter.items():
                new_counter[val + node.val] = count

            if node.val not in new_counter:
                new_counter[node.val] = 1
            else:
                new_counter[node.val] += 1

            if node.left is not None:
                exploreNode(node.left, new_counter)

            if node.right is not None:
                exploreNode(node.right, new_counter)

        exploreNode(root, {})
        return ans
