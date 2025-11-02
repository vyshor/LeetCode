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
    vector<int> order;

    TreeNode* recur(int i, int j) {
        if (i > j || i >= order.size()) return nullptr;
        if (i == j) return new TreeNode(order[i]);

        TreeNode* node = new TreeNode(order[i]);
        int k = i+1;
        while (k < order.size() && order[k] < order[i]) {
            k++;
        }
        node->left = recur(i+1, k-1);
        node->right = recur(k, j);
        return node;
    }

    TreeNode* bstFromPreorder(vector<int>& preorder) {
        order = std::move(preorder);
        int n = order.size();
        return recur(0, n-1);
    }
};
