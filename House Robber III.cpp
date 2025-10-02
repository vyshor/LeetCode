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
    pair<int, int> recur(TreeNode* node) {
        if (!node) return {0, 0};

        auto [lrob, lnorob] = recur(node->left);
        auto [rrob, rnorob] = recur(node->right);

        int rob = node->val + lnorob + rnorob;
        int norob = max(rrob, rnorob) + max(lrob, lnorob);
        return {rob, norob};
    }

    int rob(TreeNode* root) {
        auto [rob, norob] = recur(root);
        return max(rob, norob);
    }
};
