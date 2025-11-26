class Solution {
public:
    int numberOfPaths(vector<vector<int>>& grid, int k) {
        constexpr int mod = 1e9 + 7;
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<vector<int>>> dp(m, vector<vector<int>>(n, vector<int>(k, 0)));
        int r = grid[0][0] % k;
        dp[0][0][r] = 1;
        int prev = r;
        for (int i{1}; i < m; ++i) {
            int new_r = (prev+grid[i][0]) % k;
            dp[i][0][new_r] = 1;
            prev = new_r;
        }

        prev = r;
        for (int j{1}; j < n; ++j) {
            int new_r = (prev+grid[0][j]) % k;
            dp[0][j][new_r] = 1;
            prev = new_r;
        }

        for (int i{1}; i < m; ++i) {
            for (int j{1}; j < n; ++j) {
                int val = grid[i][j] % k;
                for (int k2{0}; k2 < k; ++k2) {
                    int offset = (k-val+k2) % k;
                    dp[i][j][k2] += dp[i-1][j][offset] + dp[i][j-1][offset];
                    dp[i][j][k2] %= mod;
                }
            }
        }
        return dp[m-1][n-1][0];
    }
};
