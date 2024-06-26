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
    void read(TreeNode* node) {
        if (!node) return;
        read(node->left);
        arr_.push_back(node->val);
        read(node->right);
    }

    TreeNode* balance(int left, int right) {
        if (left == right) {
            TreeNode* node = new TreeNode(arr_[left]);
            return node;
        }

        if (left > right) return nullptr;

        int mid = (left+right)/2;
        TreeNode* node = new TreeNode(arr_[mid]);
        node->left = balance(left, mid-1);
        node->right = balance(mid+1, right);
        return node;
    }

    TreeNode* balanceBST(TreeNode* root) {
        read(root);
        return balance(0, arr_.size()-1);
    }

    vector<int> arr_;
};

