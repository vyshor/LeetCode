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
    TreeNode* addOneRow(TreeNode* root, int val, int depth) {
        if (depth == 1) {
            TreeNode* new_root = new TreeNode(val, root, nullptr);
            return new_root;
        }

        function<void(TreeNode*, int)> exploreNode;
        exploreNode = [&exploreNode, &val] (TreeNode* node, int d) {
            if (node == nullptr) return;

            if (d == 1) {
                TreeNode* left = new TreeNode(val, node->left, nullptr);
                TreeNode* right = new TreeNode(val, nullptr, node->right);
                node->left = left;
                node->right = right;
                return;
            }

            exploreNode(node->left, d-1);
            exploreNode(node->right, d-1);
        };

        exploreNode(root, depth-1);
        return root;
    }
};
