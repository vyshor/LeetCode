class Solution {
public:

    long long getMaxFunctionValue(vector<int>& receiver, long long k) {
        int n = receiver.size();
        int64_t m = 0;
        int64_t k2 = k;
        while (k2 != 0) {
            m++;
            k2 >>= 1;
        }

        vector<vector<int>> up(m, vector<int>(n));
        vector<vector<int64_t>> dp(m, vector<int64_t>(n));

        for (int i = 0; i < n; i++) {
            up[0][i] = receiver[i];
            dp[0][i] = receiver[i];
        }


        // First layer of parent is built
        // Build layer by layer

        for (int j = 1; j < m; j++) {
            for (int i = 0; i < n; i++) {
                up[j][i] = up[j-1][up[j-1][i]];
                dp[j][i] = dp[j-1][i] + dp[j-1][up[j-1][i]];

                // j is the exponent of 2 for jumps
                // i is position
                // up[j+1][i] = up[j][up[j][i]];
                // dp[j+1][i] = dp[j][i] + dp[j][up[j][i]];

                // Most uninitive, but most logical way to understand it
                // up[j-1][i] represents ancestor, which are also precalculated
                // So summing the value of dp[j-1][i] (Sum of current pos)
                // + dp[j-1][up[j-1][i]] (Sum of ancestor, which is going to be next pos)
            }
        }

        // for (int j = 0; j < m; j++) {
        //     cout << "j=" << j;
        //     for (int i = 0; i < n; i++) {
        //         cout << " " << dp[j][i];
        //     }
        //     cout << endl;
        // }

        int64_t maxx = 0;
        for (int i = 0; i < n; i++) {
            int64_t summ = i;
            int i2 = i;
            // cout << "Start=" << i2 << endl;
            for (int64_t j = 0; j < m; j++) {
                if (k & (static_cast<int64_t>(1) << j)) {
                    summ += dp[j][i2];
                    i2 = up[j][i2];
                    // cout << "Nxt=" << i2 << endl;
                    // cout << "Summ=" << summ << endl;
                }
            }

            // cout << "End=" << i2 << endl;
            // cout << "Val=" << summ << endl;
            maxx = max(maxx, summ);
        }
        return maxx;

    }
};
