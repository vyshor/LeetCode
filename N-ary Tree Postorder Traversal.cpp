/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<int> postorder(Node* root) {
        if (root == nullptr) return {};
        vector<Node*> arr = {root};
        vector<int> ans;
        while (!arr.empty()) {
            auto node = arr.back();
            arr.pop_back();
            ans.push_back(node->val);
            for (auto child: node->children) {
                arr.push_back(child);
            }
        }
        int n = ans.size() - 1, i = 0;
        while (i < n) {
            auto tmp = ans[n];
            ans[n--] = ans[i];
            ans[i++] = tmp;
        }
        return ans;
    }
};
