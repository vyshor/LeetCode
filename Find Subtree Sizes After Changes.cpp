class Solution {
public:
    vector<vector<int>> children;
    vector<int> summ;
    string S;

    int recur(int node, vector<int>& ancestor) {
        int idx = S[node]-97;

        int prev_ancestor = ancestor[idx];
        ancestor[idx] = node;
        for (int child: children[node]) {
            int result = recur(child, ancestor);
            summ[node] += result;
        }
        ++summ[node];

        ancestor[idx] = prev_ancestor;
        if (prev_ancestor != -1) {
            summ[prev_ancestor] += summ[node];
        }
        return prev_ancestor != -1 ? 0 : summ[node];
    }

    vector<int> findSubtreeSizes(vector<int>& parent, string s) {
        int n = parent.size();
        S = std::move(s);
        children = vector<vector<int>>(n);
        summ = vector<int>(n, 0);

        for (int i = 0; i < n; ++i) {
            if (parent[i] >= 0) children[parent[i]].push_back(i);
        }

        vector<int> ancestors(26, -1);
        recur(0, ancestors);

        return std::move(summ);
    }
};
