class Solution {
public:
    int profitableSchemes(int n, int minProfit, vector<int>& group, vector<int>& profit) {
        int MOD = 1000000007;
        vector<vector<int64_t>> dp;
        dp.reserve(n+1);

        for (int i = 0; i < n+1; i++) {
            vector<int64_t> arr(minProfit+1, 0);
            dp.push_back(arr);
        }

        dp[n][minProfit] = 1;

        for (int k = 0; k < group.size(); k++) {
            int& ppl = group[k];
            int& money = profit[k];
            for (int i = 0; i < n+1; i++) {
                for (int j = 0; j < minProfit+1; j++) {
                    if (i-ppl >= 0 && dp[i][j] > 0) {
                        int new_money = max(j-money, 0);
                        dp[i-ppl][new_money] += dp[i][j];
                        dp[i-ppl][new_money] %= MOD;
                    }
                }
            }
        }

        int64_t total_count = 0;
        for (int i = 0; i< n+1; i++) total_count = (total_count+dp[i][0]) % MOD;
        return total_count;
    }
};
