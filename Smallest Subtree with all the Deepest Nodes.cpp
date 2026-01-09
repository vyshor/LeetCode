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
    int maxx{0};
    void getDepth(TreeNode* node, int depth) {
        if (!node) return;
        maxx = max(maxx, depth);
        getDepth(node->left, depth+1);
        getDepth(node->right, depth+1);
    }

    TreeNode* recur(TreeNode* node, int depth) {
        if (!node) return nullptr;
        if (depth == maxx) return node;
        TreeNode* leftDeep = recur(node->left, depth+1);
        TreeNode* rightDeep = recur(node->right, depth+1);
        if (leftDeep && rightDeep) return node;
        if (leftDeep) return leftDeep;
        if (rightDeep) return rightDeep;
        return nullptr;
    }

    TreeNode* subtreeWithAllDeepest(TreeNode* root) {
        getDepth(root, 0);
        return recur(root, 0);
    }
};
