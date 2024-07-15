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
    TreeNode* createBinaryTree(vector<vector<int>>& descriptions) {
        unordered_map<int, TreeNode*> dp;
        unordered_map<int, int> dp_incoming;
        for (auto desc: descriptions) {
            int p = desc[0], c = desc[1], l = desc[2];
            dp_incoming[c] += 1;
            dp_incoming[p] += 0;

            if (!dp.contains(p)) dp[p] = new TreeNode(p);
            if (!dp.contains(c)) dp[c] = new TreeNode(c);
            if (l) dp[p]->left = dp[c]; else dp[p]->right = dp[c];
        }

        for (auto [k, v]: dp_incoming) {
            if (v == 0) return dp[k];
        }
        return nullptr;
    }
};
