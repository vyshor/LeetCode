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
    unordered_map<int, TreeNode*> parents;

    void addParent(TreeNode* node, TreeNode* parent) {
        if (!node) return;

        parents[node->val] = parent;
        addParent(node->left, node);
        addParent(node->right, node);
    }

    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        addParent(root, nullptr);

        vector<int> ans;
        deque<pair<int, TreeNode*>> q;
        unordered_set<int> visited;

        q.emplace_back(0, target);

        while (q.size() > 0) {
            auto [dist, node] = q.front();
            q.pop_front();
            visited.insert(node->val);

            if (dist == k) {
                ans.push_back(node->val);
            } else {
                if (node->right && !visited.contains(node->right->val)) q.emplace_back(dist+1, node->right);
                if (node->left && !visited.contains(node->left->val)) q.emplace_back(dist+1, node->left);
                if (parents[node->val] && !visited.contains(parents[node->val]->val)) q.emplace_back(dist+1, parents[node->val]);
            }
        }

        return ans;
    }
};
