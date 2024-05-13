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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        function<bool(TreeNode*, TreeNode*)> compareTree;
        compareTree = [&compareTree] (TreeNode* a, TreeNode* b) -> bool {
            if (a == nullptr && b == nullptr) return true;
            if (a == nullptr || b == nullptr) return false;
            if (a->val != b->val) return false;
            return compareTree(a->left, b->left) && compareTree(a->right, b->right);
        };

        return compareTree(p, q);
    }
};
