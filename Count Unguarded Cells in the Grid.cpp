class Solution {
public:
    int countUnguarded(int m, int n, vector<vector<int>>& guards, vector<vector<int>>& walls) {
        vector<vector<int>> dp(m, vector<int> (n, 0));

        for (auto& arr: guards) {
            dp[arr[0]][arr[1]] = 0b0'1111;
        }
        for (auto& arr: walls) {
            dp[arr[0]][arr[1]] = 0b1'0000;
        }

        for (int i = 1; i < m; i++) {
            if (dp[i][0] != 0b1'0000) {
                dp[i][0] |= (dp[i-1][0] & 0b0'0001);
            }
        }

        for (int j = 1; j < n; j++) {
            if (dp[0][j] != 0b1'0000) {
                dp[0][j] |= (dp[0][j-1] & 0b0'0010);
            }
        }

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (dp[i][j] != 0b1'0000) {
                    dp[i][j] |= (dp[i][j-1] & 0b0'0010) | (dp[i-1][j] & 0b0'0001);
                }
            }
        }

        int count = (dp[m-1][n-1] == 0);
        for (int i = m-2; i >= 0; i--) {
            if (dp[i][n-1] != 0b1'0000) {
                dp[i][n-1] |= (dp[i+1][n-1] & 0b0'0100);
            }
            count += (dp[i][n-1] == 0);
        }

        for (int j = n-2; j >= 0; j--) {
            if (dp[m-1][j] != 0b1'0000) {
                dp[m-1][j] |= (dp[m-1][j+1] & 0b0'1000);
            }
            count += (dp[m-1][j] == 0);
        }

        for (int i = m-2; i >= 0; i--) {
            for (int j = n-2; j >= 0; j--) {
                if (dp[i][j] != 0b1'0000) {
                    dp[i][j] |= (dp[i][j+1] & 0b0'1000) | (dp[i+1][j] & 0b0'0100);
                }

                count += (dp[i][j] == 0);
            }
        }
        return count;
    }
};
