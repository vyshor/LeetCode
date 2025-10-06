class Solution {
public:
    int swimInWater(vector<vector<int>>& grid) {
        int n = grid.size();
        unordered_set<int> visited;
        vector<pair<int, int>> q;
        q.emplace_back(-grid[0][0], 0);
        int t = 0;
        while (q.size() > 0) {
            pop_heap(q.begin(), q.end());
            auto [t2, k] = q.back();
            q.pop_back();
            if (visited.contains(k)) continue;
            visited.insert(k);

            t = min(t, t2);
            int i = k >> 16;
            int j = ((1 << 16) - 1) & k;
            if (i == n-1 && j == n-1) return -t;

            vector<pair<int, int>> dirs{
                {1, 0},
                {-1, 0},
                {0, 1},
                {0, -1}
            };

            for (auto [x,y]: dirs) {
                x += i;
                y += j;
                int k2 = (x << 16) | y;
                if (x < 0 || x >= n || y < 0 || y >= n) continue;
                if (visited.contains(k2)) continue;
                q.emplace_back(-grid[x][y], k2);
                push_heap(q.begin(), q.end());
            }
        }
        return 0;
    }
};
