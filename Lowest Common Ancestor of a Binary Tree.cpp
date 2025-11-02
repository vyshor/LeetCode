/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    unordered_map<int, int> depth;
    unordered_map<int, TreeNode*> parents;

    int n;
    int max_depth = 0;
    int LOG;

    void dfs(TreeNode* parent, TreeNode* node, int d) {
        if (!node) return;

        parents[node->val] = parent;
        depth[node->val] = d;
        max_depth = max(max_depth, d);
        dfs(node, node->left, d+1);
        dfs(node, node->right, d+1);
    }

    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        dfs(root, root, 0);
        n = parents.size();

        int m2 = max_depth;
        LOG = 0;
        while (m2 != 0) {
            m2 >>= 1;
            LOG++;
        }

        // Preprocessing
        vector<unordered_map<int, TreeNode*>> up(LOG);
        for (auto [k, v]: parents) {
            up[0][k] = v;
        }

        for (int j = 1; j < LOG; j++) {
            for (auto [i, _]: parents) {
                up[j][i] = up[j-1][up[j-1][i]->val];
            }
        }

        if (depth[p->val] < depth[q->val]) {
            swap(p, q);
        }

        int k = depth[p->val] - depth[q->val];
        for (int j = 0; j < LOG; ++j) {
            if (k & (1 << j)) {
                p = up[j][p->val];
            }
        }

        if (p->val == q->val) return p;

        for (int j = LOG - 1; j >= 0; --j) {
            if (up[j][p->val] != up[j][q->val]) {
                p = up[j][p->val];
                q = up[j][q->val];
            }
        }
        return up[0][p->val];
    }
};
