class Solution {
public:
    vector<int> convert(unordered_set<int>& w) {
        vector<int> v(w.begin(), w.end());
        sort(v.begin(), v.end());
        return v;
    }
    vector<vector<int>> getAncestors(int n, vector<vector<int>>& edges) {
        vector<int> q;
        vector<int> in_edges(n, 0);
        unordered_map<int, vector<int>> pairs;
        for (auto edge: edges) {
            pairs[edge[0]].push_back(edge[1]);
            in_edges[edge[1]]++;
        }

        for (int i = 0; i < n; i++) {
            if (!in_edges[i]) q.push_back(i);
        }

        vector<unordered_set<int>> ans(n);
        while (q.size() > 0) {
            int i = q.back();
            q.pop_back();

            for (int target: pairs[i]) {
                ans[target].insert(i);
                ans[target].insert(ans[i].begin(), ans[i].end());
                if (--in_edges[target] == 0) q.push_back(target);
            }
        }

        vector<vector<int>> sorted_ans(n);
        for (int i = 0; i < n; i++) {
            sorted_ans[i] = convert(ans[i]);
        }
        return sorted_ans;
    }
};
