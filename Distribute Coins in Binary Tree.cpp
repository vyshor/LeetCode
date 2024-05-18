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
    int distributeCoins(TreeNode* root) {
        function<pair<int, int>(TreeNode*)> explore;
        explore = [&explore] (TreeNode* node) -> pair<int, int> {
            int nett = node->val - 1, cost = 0;
            if (node->left != nullptr) {
                auto [left_nett, left_cost] = explore(node->left);
                cost +=left_cost + abs(left_nett);
                nett += left_nett;
            }

            if (node->right != nullptr) {
                auto [right_nett, right_cost] = explore(node->right);
                cost += right_cost + abs(right_nett);
                nett +=right_nett;
            }

            return make_pair(nett, cost);
        };
        return explore(root).second;
    }
};
