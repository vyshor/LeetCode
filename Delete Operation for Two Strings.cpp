class Solution {
public:
    int minDistance(string word1, string word2) {
        int n1 = word1.size()+1, n2 = word2.size()+1;
        vector<vector<int>> dp(n1, vector<int>(n2, n1+n2));
        dp[0][0] = 0;
        for (int i = 1; i < n1; ++i) {
            dp[i][0] = i;
        }

        for (int j = 1; j < n2; ++j) {
            dp[0][j] = j;
        }

        for (int i = 1; i < n1; ++i) {
            for (int j = 1; j < n2; ++j) {
                dp[i][j] = min(dp[i][j], dp[i-1][j]+1);
                dp[i][j] = min(dp[i][j], dp[i][j-1]+1);
                if (word1[i-1] == word2[j-1]) {
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1]);
                }
            }
        }
        return dp[n1-1][n2-1];
    }
};
