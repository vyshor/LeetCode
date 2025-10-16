class Solution {
public:
    vector<int> avail = vector<int>(100, 0);
    unordered_map<int, int> dp;

    int recur(int i, int state) {
        if (state == 0) return 0;
        if (i < 0) return 0;

        int key = (i << 10) | state;
        if (dp.contains(key)) return dp[key];

        int choices = state & avail[i];
        if (choices == 0) {
            dp[key] = recur(i-1, state);
            return dp[key];
        }

        int maxx_val = 0;
        for (int j = 0; j < 10; j++) {
            if ((choices >> j) & 1) {
                maxx_val = max(maxx_val, recur(i-1, state ^ (1 << j)));
            }
        }
        dp[key] = maxx_val+i+1;
        return dp[key];
    }

    int maxScore(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int max_val = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int val = grid[i][j];
                max_val = max(max_val, val);
                avail[val-1] |= (1 << i);
            }
        }

        return recur(max_val-1, (1 << m)-1);
    }
};
