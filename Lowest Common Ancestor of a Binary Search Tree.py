# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        dp = {}
        dp_nodes = {}

        # dp[child.val] = parent.val
        def save_node(node, parent_val):
            if not node:
                return
            dp[node.val] = parent_val
            dp_nodes[node.val] = node
            save_node(node.left, node.val)
            save_node(node.right, node.val)

        save_node(root, '-')

        # After saving node, start crawling up
        explored_parents = {}
        p_val = p.val
        while p_val != '-':
            explored_parents[p_val] = True
            p_val = dp[p_val]

        # Crawl up for q also, but termiantes if found any explored parent
        q_val = q.val
        while q_val != '-':
            if explored_parents.get(q_val, False):
                return dp_nodes[q_val]
            else:
                q_val = dp[q_val]
        return None

# Time: O(n)
# Space: O(n)
# Runtime: 136 ms, faster than 6.09% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
# Memory Usage: 17.1 MB, less than 100.00% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.