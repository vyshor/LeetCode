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
    vector<int> visited;
    vector<int> iorder;
    vector<int> porder;
    unordered_map<int, int> mapping;
    int N;

    TreeNode* recur(int i, int j, int k) {
        if (i == j) return new TreeNode(iorder[i]);
        if (i > j) return nullptr;

        while (k >= 0) {
            int mid_val = porder[k];
            int idx = mapping[mid_val];
            if (i <= idx && idx <= j) {
                auto node = new TreeNode(mid_val);
                node->left = recur(i, idx-1, k-1);
                node->right = recur(idx+1, j, k-1);
                return node;
            }
            k--;
        }
        return nullptr;
    }

    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        N = inorder.size();
        visited = vector<int>(N, 0);
        for (int i = 0; i < N; i++) {
            mapping[inorder[i]] = i;
        }

        porder = std::move(postorder);
        iorder = std::move(inorder);
        return recur(0, N-1, N-1);
    }
};
