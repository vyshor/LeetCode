# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        count = 0

        def explore(node):
            nonlocal count, distance
            if node is None:
                return {}

            if not node.left and not node.right:
                return {0: 1}

            counter = Counter()
            left_counter = explore(node.left)
            right_counter = explore(node.right)
            for k, v in left_counter.items():
                for k2, v2 in right_counter.items():
                    if k + k2 + 2 <= distance:
                        count += v * v2

                if k + 1 < distance:
                    counter[k + 1] += v

            for k, v in right_counter.items():
                if k + 1 < distance:
                    counter[k + 1] += v

            return counter

        explore(root)
        return count
