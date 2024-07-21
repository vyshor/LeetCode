class Solution {
public:
    unordered_map<int, int> condSort(vector<vector<int>>& conds, int k) {
        vector<int> in_edges(k, 0);
        unordered_map<int, unordered_set<int>> edges;
        for (auto cond: conds) {
            int fro = cond[0]-1, to = cond[1]-1;
            if (!edges[fro].contains(to)) {
                edges[fro].insert(to);
                in_edges[to]++;
            }
        }

        vector<int> q;
        for (int i = 0; i < k; i++) {
            if (!in_edges[i]) q.push_back(i);
        }

        int count = 0;
        unordered_map<int, int> order;
        while (!q.empty()) {
            int i = q.back();
            q.pop_back();
            order[i] = count++;

            if (edges.contains(i)) {
                for (int j : edges[i]) {
                    if (--in_edges[j] == 0) q.push_back(j);
                }
            }
        }

        if (count < k) return {};
        return order;
    }

    vector<vector<int>> buildMatrix(int k, vector<vector<int>>& rowConditions, vector<vector<int>>& colConditions) {
        auto row = condSort(rowConditions, k);
        auto col = condSort(colConditions, k);
        if (row.size() == 0 || col.size() == 0) return {};

        vector<vector<int>> matrix;
        for (int i = 0; i < k; i++) {
            matrix.emplace_back(k, 0);
        }

        for (int i = 0; i < k; i++) {
            matrix[row[i]][col[i]] = i+1;
        }
        return matrix;

    }
};
