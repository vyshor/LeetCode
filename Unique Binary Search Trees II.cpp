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
    unordered_map<int, vector<TreeNode*>> dp;

    vector<TreeNode*> recur(int lower, int upper) {
        if (upper < lower) return {nullptr};

        int key = (upper << 4) | lower;
        if (dp.contains(key)) return dp[key];

        if (lower == upper) {
            auto ptr = new TreeNode(lower);
            dp[key] = {ptr};
            return dp[key];
        }

        vector<TreeNode*> children;
        for (int i = lower; i < upper+1; i++) {
            auto left_ptrs = recur(lower, i-1);
            auto right_ptrs = recur(i+1, upper);
            int total_nodes = left_ptrs.size() * right_ptrs.size();
            children.reserve(total_nodes);

            for (auto& left_ptr: left_ptrs) {
                for (auto& right_ptr: right_ptrs) {
                    children.push_back(new TreeNode(i, left_ptr, right_ptr));
                }
            }
        }
        dp[key] = children;
        return dp[key];
    }

    vector<TreeNode*> generateTrees(int n) {
        return recur(1, n);
    }
};
