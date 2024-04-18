class Solution {
public:
    int getKey(int i, int j) {
        return (i << 10) | j;
    }

    pair<int, int> returnKey(int key) {
        int i = key >> 10;
        int j = ((1 << 10) - 1) & key;
        return make_pair(i, j);
    }

    int islandPerimeter(vector<vector<int>>& grid) {
        unordered_set<int> visited;
        int perimeter = 0;
        int n = grid.size(), m = grid[0].size();
        vector<pair<int, int>> q;

        bool to_break = false;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j]) {
                    q.push_back(make_pair(i, j));
                    to_break = true;
                    break;
                }
            }

            if (to_break) break;
        }

        while (q.size() > 0) {
            auto p = q.back();
            int i = p.first, j = p.second;
            int key = getKey(i, j);
            q.pop_back();

            if (visited.contains(key)) continue;

            visited.insert(key);
            vector<pair<int, int>> pairs{{i-1, j}, {i+1, j}, {i, j-1}, {i, j+1}};
            for (auto & xy: pairs) {
                int x = xy.first, y = xy.second;
                if (visited.contains(getKey(x, y))) continue;

                if (0 <= x && x < n && 0 <= y && y < m && grid[x][y]) {
                    q.push_back(xy);
                } else {
                    perimeter++;
                }
            }
        }
        return perimeter;
    }
};
