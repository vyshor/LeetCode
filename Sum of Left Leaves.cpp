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
    int sumOfLeftLeaves(TreeNode* root) {
        int summ = 0;
        function<void(TreeNode*, bool)> exploreNode;
        exploreNode = [&summ, &exploreNode] (TreeNode* node, bool is_left) -> void {
            if (node == nullptr) {
                return;
            }

            if (node->left == nullptr && node->right == nullptr && is_left) {
                summ += node->val;
            }

            exploreNode(node->left, true);
            exploreNode(node->right, false);
        };

        exploreNode(root, false);
        return summ;
    }
};
