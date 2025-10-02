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
    vector<int> vals;

    void recur(TreeNode* node) {
        if (!node) return;
        recur(node->left);
        vals.push_back(node->val);
        recur(node->right);
    }

    int minDiffInBST(TreeNode* root) {
        recur(root);

        int n = vals.size();
        int minn = INT_MAX;
        for (int i = 0; i < n-1; i++) {
            minn = min(minn, vals[i+1]-vals[i]);
        }
        return minn;
    }
};
