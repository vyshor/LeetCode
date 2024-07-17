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
    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
        vector<TreeNode*> nodes;
        unordered_set<int> to_del(to_delete.begin(), to_delete.end());
        auto dummy = new TreeNode(0, root, nullptr);
        function<void(TreeNode*, TreeNode*, bool)> explore;
        explore = [&explore, &nodes, &to_del] (TreeNode* node, TreeNode* parent, bool left) {
            if (!node) return;

            explore(node->left, node, true);
            explore(node->right, node, false);

            if (to_del.contains(node->val)) {
                if (left) parent->left = nullptr;
                else parent->right = nullptr;

                if (node->left) nodes.push_back(node->left);
                if (node->right) nodes.push_back(node->right);
            }
        };

        explore(root, dummy, true);
        if (dummy->left) nodes.push_back(dummy->left);
        return nodes;
    }
};
