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
    TreeNode* replaceValueInTree(TreeNode* root) {
        unordered_map<int, unordered_map<TreeNode*, int>> summ;
        unordered_map<int, unordered_map<TreeNode*, vector<TreeNode*>>> children;
        function<void(TreeNode*, TreeNode*, int)> recur;
        recur = [&recur, &summ, &children] (TreeNode* node, TreeNode* parent, int level = 0) {
            if (!node) return;

            if (level == 0) {
                summ[level] = {{0, 0}};
                children[level] = {{nullptr, {node}}};
            } else {
                if (!summ[level].contains(parent)) {
                    summ[level][parent] = node->val;
                    children[level][parent] = {node};
                } else {
                    summ[level][parent] += node->val;
                    children[level][parent].push_back(node);
                }
            }
            recur(node->left, node, level+1);
            recur(node->right, node, level+1);
        };
        recur(root, nullptr, 0);
        for (auto [level, d]: summ) {
            int total_count = 0;
            for (auto [_, count]: d) {
                total_count += count;
            }

            for (auto [parent, count]: d) {
                int corrected = total_count - count;
                for (auto node: children[level][parent]) node->val = corrected;
            }
        }
        return root;
    }
};
