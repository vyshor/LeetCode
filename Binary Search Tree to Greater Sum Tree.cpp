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
    TreeNode* bstToGst(TreeNode* root) {
        function<int(TreeNode*, int)> check;
        check = [&check] (TreeNode* node, int summ) -> int {
            if (node == nullptr) return summ;

            summ = check(node->right, summ);
            summ += node->val;
            node->val = summ;
            return check(node->left, summ);
        };
        check(root, 0);
        return root;
    }
};
