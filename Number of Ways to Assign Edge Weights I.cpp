class Solution {
public:
    int determine_depth(vector<vector<int>>& edges) {
        // BFS
        unordered_map<int, vector<int>> connections;
        int n = 0;
        for (auto& edge: edges) {
            int u = edge[0], v= edge[1];
            connections[u].push_back(v);
            connections[v].push_back(u);
            n = max(n, u);
            n = max(n, v);
        }

        vector<int> visited(n, 0);
        visited[0] = 1;

        int max_depth = 0;
        deque<pair<int, int>> q;
        q.emplace_back(1, 0);
        while (q.size() > 0) {
            auto [node, depth] = q.front();
            q.pop_front();
            max_depth = max(max_depth, depth);
            for (int child: connections[node]) {
                if (visited[child-1]) continue;
                visited[child-1] = 1;

                q.emplace_back(child, depth+1);
            }
        }
        return max_depth;
    }

    int assignEdgeWeights(vector<vector<int>>& edges) {
        int MOD = 1e9 + 7;
        int max_depth = determine_depth(edges);
        // cout << "max_depth: " << max_depth << endl;
        int count = 1;
        for (int i = 0; i < max_depth-1; i++) {
            count <<= 1;
            if (count > MOD) {
                count %= MOD;
            }
        }
        return count;
    }
};
