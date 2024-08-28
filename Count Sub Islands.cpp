class Solution {
public:
    int countSubIslands(vector<vector<int>>& grid1, vector<vector<int>>& grid2) {
        int n = grid2.size(), m = grid2[0].size();
        set<pair<int, int>> visited;
        int islands = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                auto p = make_pair(i, j);
                if (visited.count(p) || grid2[i][j] == 0) continue;

                vector<pair<int, int>> q = {{i, j}};
                bool is_island = true;
                while (!q.empty()) {
                    auto [x, y] = q.back();
                    q.pop_back();
                    auto p2 = make_pair(x, y);
                    if (visited.contains(p2)) continue;
                    visited.insert(p2);

                    if (grid1[x][y] == 0) is_island = false;
                    vector<pair<int, int>> dirs = {
                        {x-1, y},
                        {x+1, y},
                        {x, y-1},
                        {x, y+1}
                    };

                    for (auto [x2, y2]: dirs) {
                        if (x2 >= n || x2 < 0 || y2 >= m || y2 < 0 || grid2[x2][y2] == 0) continue;
                        q.emplace_back(x2, y2);
                    }
                }
                if (is_island) islands++;
            }
        }
        return islands;
    }
};
