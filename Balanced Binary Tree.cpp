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
    int recur(TreeNode* node) {
        if (!node) return 0;
        int left = recur(node->left);
        int right = recur(node->right);
        if (left == -3 || right == -3 || abs(left-right) > 1) return -3;
        return max(left, right)+1;
    }
    bool isBalanced(TreeNode* root) {
        return recur(root) != -3;
    }
};
