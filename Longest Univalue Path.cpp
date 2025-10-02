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
    int maxx = 1;

    pair<int, int> recur(TreeNode* node) {
        if (!node) return {0, 0};
        auto [lval, lcount] = recur(node->left);
        auto [rval, rcount] = recur(node->right);
        if (node->val == lval && lval == rval) maxx = max(maxx, lcount + rcount + 1);

        int max_path = 1;
        if (node->val == lval) max_path += lcount;
        if (node->val == rval) max_path = max(max_path, 1+rcount);
        maxx = max(maxx, max_path);

        return {node->val, max_path};
    }

    int longestUnivaluePath(TreeNode* root) {
        recur(root);
        return maxx-1;
    }
};