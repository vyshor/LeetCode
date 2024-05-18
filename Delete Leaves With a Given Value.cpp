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
    TreeNode* removeLeafNodes(TreeNode* root, int target) {
        unordered_map<TreeNode*, pair<TreeNode*, bool>> parents;
        TreeNode dummy(0, root, nullptr);
        function<void(TreeNode*)> explore;
        explore = [&explore, &target, &parents] (TreeNode* node) -> void {
            if (node->left == nullptr && node->right == nullptr && node->val == target) {
                auto parent_pair = parents[node];
                TreeNode* parent = parent_pair.first;
                bool is_left = parent_pair.second;
                if (is_left) parent->left = nullptr;
                else parent->right = nullptr;

                parents.erase(node);
                explore(parent);
            }

            if (node->left != nullptr) {
                parents[node->left] = make_pair(node, true);
                explore(node->left);
            }

            if (node->right != nullptr) {
                parents[node->right] = make_pair(node, false);
                explore(node->right);
            }
        };

        explore(&dummy);
        return dummy.left;
    }
};
