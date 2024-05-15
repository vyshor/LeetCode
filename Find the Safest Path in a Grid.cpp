class Solution {
public:
    int maximumSafenessFactor(vector<vector<int>>& grid) {
        int n = grid.size();
        if (grid[0][0] || grid[n-1][n-1]) return 0;

        vector<vector<int>> dp;
        for (int i = 0; i < n; i++) {
            dp.emplace_back(n, 2*n);
        }

        deque<pair<int, pair<int, int>>> q;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j]) q.push_back(make_pair(0, make_pair(i, j)));
            }
        }

        while (!q.empty()) {
            auto kpair = q.front();
            q.pop_front();
            int dist = kpair.first, i = kpair.second.first, j = kpair.second.second;

            if (dp[i][j] != 2*n) continue;

            dp[i][j] = dist;
            vector<pair<int, int>> directions {
                {i-1, j},
                {i+1, j},
                {i, j-1},
                {i, j+1},
            };
            for (auto xy: directions) {
                int x = xy.first, y = xy.second;
                if (0 <= x && x < n && 0 <= y && y < n && dp[x][y] == 2*n) q.push_back(make_pair(dist+1, make_pair(x, y)));
            }

        }


        vector<tuple<int, int, int>> path{
            {dp[0][0], 0, 0}
        };
        unordered_set<int> walked;
        while (!path.empty()) {
            pop_heap(path.begin(), path.end());
            auto t = path.back();
            int dist = get<0>(t), i = get<1>(t), j = get<2>(t);
            // cout << "Dist: " <<  dist << " i: " << i << " j: " << j << endl;
            path.pop_back();

            int key = (i << 10) | j;
            if (walked.contains(key)) continue;
            walked.insert(key);

            if (i == n-1 && j == n-1) return dist;

            vector<pair<int, int>> directions {
                {i-1, j},
                {i+1, j},
                {i, j-1},
                {i, j+1},
            };

            for (auto xy: directions) {
                int x = xy.first, y = xy.second;
                if (0 <= x && x < n && 0 <= y && y < n && !walked.contains((x << 10) | y)) {
                    tuple<int, int, int> new_t{min(dist, dp[x][y]), x, y};
                    path.push_back(new_t);
                    push_heap(path.begin(), path.end());
                }
            }
        }
        return 0;
    }
};