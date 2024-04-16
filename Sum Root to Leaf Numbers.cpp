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
    int sumNumbers(TreeNode* root) {
        int summ = 0;

        function<void(TreeNode*, string)> exploreNode;
        exploreNode = [&summ, &exploreNode] (TreeNode* node, string path) {
            if (node == nullptr) return;
            path += to_string(node->val);
            if (node->left == nullptr && node->right == nullptr) {
                summ += stoi(path);
                return;
            }
            exploreNode(node->left, path);
            exploreNode(node->right, path);
        };

        exploreNode(root, "");
        return summ;
    }
};
