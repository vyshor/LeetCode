struct Node {
    int child_count = 0;
    int val = 0;
    vector<Node*> children;

    pair<int, int> recur(Node* fro, int k) {
        int parts = 0;
        int r = val;
        for (int i{0}; i < child_count; ++i) {
            if (fro == children[i]) continue;
            // cout << "i=" << i << " child_count=" << child_count << endl;
            auto [p1, r1] = children[i]->recur(this, k);
            parts += p1;
            r += r1;
        }
        r %= k;
        if (r == 0) ++parts;
        return {parts, r};
    }
};

class Solution {
public:
    int maxKDivisibleComponents(int n, vector<vector<int>>& edges, vector<int>& values, int k) {
        vector<Node> nodes(n);
        for (int i{0}; i < n; ++i) {
            nodes[i].val = values[i] % k;
        }
        for (auto& edge: edges) {
            Node& a = nodes[edge[0]];
            Node& b = nodes[edge[1]];
            a.children.push_back(&b);
            ++a.child_count;
            b.children.push_back(&a);
            ++b.child_count;
        }

        for (int i{0}; i < n; ++i) {
            if (nodes[i].child_count <= 2) {
                auto [p, r] = nodes[i].recur(nullptr, k);
                return p;
            }
        }
        return 0;
    }
};
