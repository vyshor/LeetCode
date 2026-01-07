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
    int64_t summ{0};
    vector<int64_t> node_summs;

    int64_t recur(TreeNode* node) {
        if (!node) return 0;

        int64_t left_summ = recur(node->left);
        int64_t right_summ = recur(node->right);
        int64_t curr_summ = left_summ + right_summ + node->val;
        node_summs.push_back(curr_summ);
        return curr_summ;
    }

    int maxProduct(TreeNode* root) {
        constexpr int64_t mod = 1e9+7;
        summ = recur(root);
        int64_t maxx{0};
        for (int64_t val: node_summs) {
            int64_t curr_maxx = (summ - val) * val;
            maxx = max(maxx, curr_maxx);
        }
        return maxx % mod;
    }
};
