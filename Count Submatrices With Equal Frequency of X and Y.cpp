class Solution {
public:
    int numberOfSubmatrices(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
        vector<vector<int>> hasX(m+1, vector<int>(n+1, 0));
        int count = 0;
        for (int i = 1; i < m+1; i++) {
            for (int j = 1; j < n+1; j++) {
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + (grid[i-1][j-1] == 'X') - (grid[i-1][j-1] == 'Y');
                hasX[i][j] |= hasX[i-1][j] | hasX[i][j-1] | (grid[i-1][j-1] == 'X');
                count += (dp[i][j] == 0 && hasX[i][j]);
            }
        }
        return count;
    }
};
