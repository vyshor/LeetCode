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
    int countPairs(TreeNode* root, int distance) {
        int count = 0;
        function<unordered_map<int, int>(TreeNode*)> explore;
        explore = [&explore, &count, &distance] (TreeNode* node) -> unordered_map<int, int> {
            if (!node) return {};

            if (!node->left && !node->right) return {{0, 1}};

            unordered_map<int, int> counter;
            auto left_counter = explore(node->left);
            auto right_counter = explore(node->right);
            for (auto [k, v]: left_counter) {
                for (auto [k2, v2]: right_counter) {
                    if (k+k2+2 <= distance) count += v * v2;
                }

                if (k+1 < distance) counter[k+1] += v;
            }

            for (auto [k, v]: right_counter) {
                if (k+1 < distance) counter[k+1] += v;
            }
            return counter;
        };
        explore(root);
        return count;
    }
};
