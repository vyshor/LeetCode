/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool evaluateTree(TreeNode* root) {
        function<bool(TreeNode*)> explore;
        explore = [&explore] (TreeNode* node) -> bool {
            if (node->left == nullptr && node->right == nullptr) return node->val;
            else if (node->val == 2) return explore(node->left) || explore(node->right);
            return explore(node->left) && explore(node->right);
        };
        return explore(root);
    }
};
