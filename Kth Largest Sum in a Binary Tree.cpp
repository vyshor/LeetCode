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
    long long kthLargestLevelSum(TreeNode* root, int k) {
        vector<int64_t> summ;
        function<void(TreeNode*, int)> recur;
        recur = [&recur, &summ] (TreeNode* node, int level) {
            if (!node) return;

            if (summ.size() == level) summ.push_back(node->val);
            else summ[level] += node->val;
            recur(node->left, level+1);
            recur(node->right, level+1);
        };
        recur(root, 0);
        if (summ.size() < k) return -1;
        sort(summ.begin(), summ.end());
        return summ[summ.size()-k];
    }
};
