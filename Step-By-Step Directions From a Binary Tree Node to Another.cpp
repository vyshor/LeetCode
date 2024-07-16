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
    string getDirections(TreeNode* root, int startValue, int destValue) {
        vector<char> path;
        string start_path, dest_path;
        function<void(TreeNode*)> explore;
        explore = [&explore, &path, &startValue, &destValue, &start_path, &dest_path] (TreeNode* node) {
            if (!node) return;

            if (node->val == startValue) {
                string p(path.begin(), path.end());
                start_path = p;
            }
            if (node->val == destValue) {
                string p(path.begin(), path.end());
                dest_path = p;
            }

            path.push_back('L');
            explore(node->left);
            path.pop_back();

            path.push_back('R');
            explore(node->right);
            path.pop_back();
        };

        explore(root);
        int n1 = min(start_path.size(), dest_path.size());
        int i = 0;
        while (i < n1) {
            if (start_path[i] == dest_path[i]) i++;
            else break;
        }

        string start(start_path.size()-i, 'U');
        string final_path = start + dest_path.substr(i);
        return final_path;
    }
};
