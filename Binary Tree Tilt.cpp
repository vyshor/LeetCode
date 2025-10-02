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
    int summ = 0;

    int recur(TreeNode* node) {
        if (!node) return 0;

        int lsum = recur(node->left);
        int rsum = recur(node->right);
        summ += abs(lsum-rsum);

        return node->val + lsum + rsum;
    }

    int findTilt(TreeNode* root) {
        recur(root);
        return summ;
    }
};