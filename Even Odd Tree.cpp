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
    bool isEvenOddTree(TreeNode* root) {
        vector<vector<int>> levels;
        function<bool(TreeNode*, int)> exploreNode;
        exploreNode = [&levels, &exploreNode] (TreeNode* node, int depth) -> bool {
            if (!node) return true;

            if (levels.size() == depth) {
                vector<int> new_level;
                levels.push_back(new_level);
            }

            if (levels.at(depth).size() > 0) {
                int last_num = levels.at(depth).back();
                if ((depth & 1) == 1) {
                    if (last_num <= node->val) return false;
                } else {
                    if (last_num >= node->val) return false;
                }
            }

            if ((depth & 1) == 1) {
                if ((node->val & 1) == 1) return false;
            } else {
                if ((node->val & 1) == 0) return false;
            }

            levels.at(depth).push_back(node->val);
            return (exploreNode(node->left, depth+1) && exploreNode(node->right, depth+1));
        };

        return exploreNode(root, 0);
    }
};
