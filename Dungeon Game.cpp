class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        int m = dungeon.size();
        int n = dungeon[0].size();
        vector<vector<int>> dp(m, vector<int>(n, INT_MAX));
        dp[m-1][n-1] = max(1 - dungeon[m-1][n-1], 1);
        for (int i = m-1; i >= 0; i--) {
            for (int j = n-1; j >= 0; j--) {
                if (i > 0) {
                    if (dp[i-1][j] > 0) {
                        dp[i-1][j] = min(dp[i-1][j], max(dp[i][j]-dungeon[i-1][j], 1));
                    } else {
                        dp[i-1][j] = min(dp[i-1][j], dp[i][j]+dungeon[i-1][j]);
                    }
                }

                if (j > 0) {
                    if (dp[i][j-1] > 0) {
                        dp[i][j-1] = min(dp[i][j-1], max(dp[i][j]-dungeon[i][j-1], 1));
                    } else {
                        dp[i][j-1] = min(dp[i][j-1], dp[i][j]+dungeon[i][j-1]);
                    }
                }
            }
        }
        return dp[0][0];
    }
};
