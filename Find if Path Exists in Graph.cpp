class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        if (source == destination) return true;

        unordered_map<int, unordered_set<int>> paths;
        for (auto& edge : edges) {
            int u = edge[0], v = edge[1];
            if (!paths.contains(u)) paths[u] = unordered_set<int>({v});
            else paths[u].insert(v);

            if (!paths.contains(v)) paths[v] = unordered_set<int>({u});
            else paths[v].insert(u);
        }

        deque<int> q;
        q.push_back(source);
        unordered_set<int> visited({source});
        while (q.size() > 0) {
            int i = move(q.front());
            q.pop_front();

            if (!paths.contains(i)) continue;

            for (auto & dst: paths[i]) {
                if (visited.contains(dst)) continue;
                if (dst == destination) return true;
                q.push_back(dst);
                visited.insert(dst);
            }
        }
        return false;
    }
};
