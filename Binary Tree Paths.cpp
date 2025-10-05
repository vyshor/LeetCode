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
    vector<string> ans;
    void recur(TreeNode* node, string& path, bool is_root = false) {
        if (!node) return;

        string new_path;
        if (is_root) {
            new_path = to_string(node->val);
        } else {
            new_path = path + "->" + to_string(node->val);;
        }

        recur(node->left, new_path);
        recur(node->right, new_path);
        if (!node->left && !node->right) ans.push_back(new_path);
    }

    vector<string> binaryTreePaths(TreeNode* root) {
        string path = "";
        recur(root, path, true);
        return ans;
    }
};
