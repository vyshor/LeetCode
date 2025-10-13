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
    unordered_map<int, int> counter;

    int recur(TreeNode* node) {
        if (!node) return 0;

        int summ = node->val;
        summ += recur(node->left) + recur(node->right);
        counter[summ]++;
        return summ;
    }
    vector<int> findFrequentTreeSum(TreeNode* root) {
        recur(root);

        int maxx_freq = 0;
        vector<int> ans;
        for (auto [k, v]: counter) {
            if (v > maxx_freq) {
                maxx_freq = v;
                ans = {k};
            } else if (v == maxx_freq) {
                ans.push_back(k);
            }
        }
        return ans;
    }
};