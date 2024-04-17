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
    string smallestFromLeaf(TreeNode* root) {

        function<deque<int>(TreeNode*, deque<int>&)> exploreNode;
        exploreNode = [&exploreNode] (TreeNode* node, deque<int>& path) -> deque<int> {
            if (node == nullptr) return path;

            path.push_front(node->val);
            if (node->left && node->right) {
                deque<int> left_copy(path);
                deque<int> right_copy(path);
                auto left_path = exploreNode(node->left, left_copy);
                auto right_path = exploreNode(node->right, right_copy);
                return min(left_path, right_path);
            } else if (node->left) return exploreNode(node->left, path);
            else if (node->right) return exploreNode(node->right, path);
            else return path;
        };

        deque<int> q;
        auto arr = exploreNode(root, q);
        stringstream ss;
        for (int& num: arr) {
            ss << (char) (num+97);
        }
        return ss.str();
    }
};
