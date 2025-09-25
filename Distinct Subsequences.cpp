class Solution {
public:
void printV(vector<vector<int>>& v) {
  	for (auto i: v) {
        for (auto j: i) {
            cout << j << " ";
        }
        cout << endl;
    }
  	cout << endl;
}

    int numDistinct(string s, string t) {
        int n = s.size();
        int m = t.size();
        vector<vector<uint64_t>> dp((n+1), vector<uint64_t>(m+1, 0));
        dp[0][0] = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m+1; j++) {
                if (j < m && s[i] == t[j]) {
                    // Consume current char
                    dp[i+1][j+1] += dp[i][j];
                }
                // Skip current char
                dp[i+1][j] += dp[i][j];
            }
        }
        // printV(dp);

        return dp[n][m];
    }
};
