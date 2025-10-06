class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        vector<vector<int>> dp(m+1, vector<int>(n+1, 0));

        for (string& s: strs) {
            int ones = 0;
            for (char ch: s) {
                ones += (ch == '1');
            }
            int zeroes = s.size() - ones;
            // cout << "ones " << ones << " zeroes " << zeroes << endl;

            for (int i = zeroes; i <= m; i++) {
                for (int j = ones; j <= n ; j++) {
                    dp[i-zeroes][j-ones] = max(dp[i-zeroes][j-ones], dp[i][j]+1);
                }
            }

            // for (int i = 0; i <= m; i++) {
            // cout << "i=" << i << "|";
            // for (int j = 0; j <= n ; j++) {
            //     cout << dp[i][j] << " ";
            //     // maxx = max(maxx, dp[i][j]);
            // }
            // cout << endl;
            // }
        }

        int maxx = 0;
        for (int i = 0; i <= m; i++) {
            // cout << "i=" << i << "|";
            for (int j = 0; j <= n ; j++) {
                // cout << dp[i][j] << " ";
                maxx = max(maxx, dp[i][j]);
            }
            // cout << endl;
        }
        return maxx;
    }
};
