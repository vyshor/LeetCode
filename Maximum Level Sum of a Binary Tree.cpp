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
    vector<int> levelSum;

    void recur(TreeNode* node, int level) {
        if (!node) return;
        if (levelSum.size() <= level) {
            levelSum.push_back(0);
        }
        levelSum[level] += node->val;
        recur(node->left, level+1);
        recur(node->right, level+1);
    }

    int maxLevelSum(TreeNode* root) {
        recur(root, 0);
        int n = levelSum.size();
        int summ = levelSum[0];
        int idx = 0;
        for (int i{1}; i < n; ++i) {
            if (levelSum[i] > summ) {
                summ = levelSum[i];
                idx = i;
            }
        }
        return idx+1;
    }
};
