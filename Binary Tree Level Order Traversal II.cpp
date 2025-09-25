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
    vector<vector<int>> results;

    void recur(TreeNode* node, int height = 0) {
        if (!node) return;

        if (results.size() < height+1) {
            results.push_back({});
        }
        recur(node->left, height+1);
        results[height].push_back(node->val);
        recur(node->right, height+1);
    }

    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        recur(root);
        vector<vector<int>> answers;
        int n = results.size();
        for (int i = n-1; i >= 0; i--) {
            answers.push_back(move(results[i]));
        }
        return answers;
    }
};
