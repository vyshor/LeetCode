# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def transverse(node, low, high, num, depth, intended_depth):
            if node is None:
                return None

            if node.left is None and node.right is None:
                if depth < intended_depth:
                    return None
                return node

            mid = (low + high) / 2
            if num < mid:
                return transverse(node.left, low, int(mid), num, depth + 1, intended_depth)
            else:
                return transverse(node.right, int(mid) + 1, high, num, depth + 1, intended_depth)

        # Get last level
        level = 1
        node = root
        while node.left is not None:
            node = node.left
            level += 1

        low, high = 2 ** (level - 1), 2 ** level - 1
        maxx = low

        left, right = low, high

        while left <= right:
            mid = (left + right) // 2

            found_node = transverse(root, low, high, mid, 1, level)
            if found_node is not None:
                maxx = max(maxx, mid)
                left = mid + 1
            else:
                right = mid - 1

        return maxx
