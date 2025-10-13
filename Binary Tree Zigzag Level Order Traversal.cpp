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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> ans;
        vector<TreeNode*> nodes;
        nodes.push_back(root);
        int reverse_order = 0;

        while (nodes.size() > 0) {
            vector<TreeNode*> next_nodes;
            vector<int> layer;
            for (auto node: nodes) {
                if (!node) continue;
                layer.push_back(node->val);
                next_nodes.push_back(node->left);
                next_nodes.push_back(node->right);
            }
            if (reverse_order) std::reverse(layer.begin(), layer.end());

            reverse_order ^= 1;
            nodes = std::move(next_nodes);
            if (layer.size() > 0) ans.push_back(std::move(layer));
        }
        return ans;
    }
};
