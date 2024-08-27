class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start_node, int end_node) {
        unordered_map<int, unordered_map<int, double>> dp;
        int i = 0;
        for (auto edge: edges) {
            int u = edge[0], v = edge[1];
            double prob = succProb[i++];
            dp[u][v] = prob;
            dp[v][u] = prob;
        }

        unordered_set<int> visited;
        vector<pair<double, int>> q = {{1., start_node}};
        while (!q.empty()) {
            pop_heap(q.begin(), q.end());
            auto [prob, node] = q.back();
            q.pop_back();
            if (node == end_node) return prob;
            if (visited.count(node)) continue;
            visited.insert(node);
            if (!dp.contains(node)) continue;
            for (auto [other, cost]: dp[node]) {
                if (!visited.contains(other)) {
                    q.emplace_back(cost * prob, other);
                    push_heap(q.begin(), q.end());
                }
            }
        }
        return 0.;
    }
};
