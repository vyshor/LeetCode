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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<TreeNode*> arr = {root};
        deque<int> ans;
        while (!arr.empty()) {
            auto node = arr.back();
            arr.pop_back();
            if (node != nullptr) {
                ans.push_front(node->val);
                arr.push_back(node->left);
                arr.push_back(node->right);
            }
        }
        vector<int> a(ans.begin(), ans.end());
        return a;
    }
};
