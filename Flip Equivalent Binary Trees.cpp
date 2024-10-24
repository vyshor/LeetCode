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
    bool flipEquiv(TreeNode* root1, TreeNode* root2) {
        function<bool(TreeNode*, TreeNode*)> recur;
        recur = [&recur] (TreeNode* node1, TreeNode* node2) -> bool {
            if (node1 == nullptr && node2 == nullptr) return true;
            if (node1 == nullptr || node2 == nullptr) return false;
            if (node1->val != node2->val) return false;
            if (!node1->left && !node2->right) return recur(node1->right, node2->left);
            if (!node1->right && !node2->left) return recur(node1->left, node2->right);
            // cout << node2->left << endl;
            if (node1->left && node2->left && node1->left->val != node2->left->val) return recur(node1->left, node2->right) && recur(node1->right, node2->left);
            return recur(node1->left, node2->left) && recur(node1->right, node2->right);
        };
        return recur(root1, root2);
    }
};
