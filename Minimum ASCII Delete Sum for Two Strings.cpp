class Solution {
public:
    int minimumDeleteSum(string s1, string s2) {
        int n1 = s1.size(), n2 = s2.size();
        int maxx{0};
        for (int ch: s1) {
            maxx += ch;
        }
        for (int ch: s2) {
            maxx += ch;
        }
        vector<vector<int>> dp(n1+1, vector<int>(n2+1, maxx));
        dp[0][0] = 0;
        for (int i{0}; i < n1+1; ++i) {
            for (int j{0}; j < n2+1; ++j) {
                if (s1[i] == s2[j] && i < n1 && j < n2) {
                    dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j]);
                }
                if (i < n1) dp[i+1][j] = min(dp[i+1][j], dp[i][j]+s1[i]);
                if (j < n2) dp[i][j+1] = min(dp[i][j+1], dp[i][j]+s2[j]);
            }
        }

        // for (int i{0}; i < n1+1; ++i) {
        //     for (int j{0}; j < n2+1; ++j) {
        //         std::cout << ' ' << dp[i][j];
        //     }
        //     std::cout << '\n';
        // }
        return dp[n1][n2];
    }
};
