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
    vector<TreeNode*> nodes;
    void recur(TreeNode* node) {
        if (!node) return;

        recur(node->left);
        nodes.push_back(node);
        recur(node->right);
    }

    void recoverTree(TreeNode* root) {
        recur(root);

        int n = nodes.size();
        if (n == 2) {
            int tmp = nodes[0]->val;
            nodes[0]->val = nodes[1]->val;
            nodes[1]->val = tmp;
            return;
        }
        TreeNode* wrongA, *wrongB;
        for (int i = 1; i < n; i++) {
            if (nodes[i-1]->val > nodes[i]->val){
                wrongA = nodes[i-1];
                break;
            }
        }

        for (int i = n-2; i > -1; i--) {
            if (nodes[i]->val > nodes[i+1]->val){
                wrongB = nodes[i+1];
                break;
            }
        }

        int tmp = wrongA->val;
        wrongA->val = wrongB->val;
        wrongB->val = tmp;
    }
};