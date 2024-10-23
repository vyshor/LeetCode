# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        summ = {}
        children = {}

        def recur(node, parent, level=0):
            nonlocal summ, children
            if node is None:
                return

            if level == 0:
                summ[level] = {0: 0}
                children[level] = {0: [node]}
            else:
                if level not in summ:
                    summ[level] = {}
                    children[level] = {}
                parent_id = id(parent)
                if parent_id not in summ[level]:
                    summ[level][parent_id] = node.val
                    children[level][parent_id] = [node]
                else:
                    summ[level][parent_id] += node.val
                    children[level][parent_id].append(node)

            recur(node.left, node, level + 1)
            recur(node.right, node, level + 1)

        recur(root, None)
        for level, d in summ.items():
            total_count = 0
            for count in d.values():
                total_count += count

            for parent_id, count in d.items():
                corrected = total_count - count
                for node in children[level][parent_id]:
                    node.val = corrected
        return root

