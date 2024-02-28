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
    int findBottomLeftValue(TreeNode* root) {
        int max_depth = 0;
        int val = root->val;

        function<void(TreeNode*, int)> exploreNode;
        exploreNode = [&max_depth, &val, &exploreNode] (TreeNode* node, int depth) -> void {
            if (!node) return;

            if (depth > max_depth) {
                max_depth = depth;
                val = node->val;
            }

            exploreNode(node->left, depth+1);
            exploreNode(node->right, depth+1);
        };

        exploreNode(root, 0);
        return val;
    }
};
