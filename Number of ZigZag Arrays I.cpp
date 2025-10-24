class Solution {
public:
    static constexpr int MOD = 1e9 + 7;

    int zigZagArrays(int n, int l, int r) {
        int diff = r-l+1;
        vector<int> dp(diff);
        std::iota(dp.begin(), dp.end(), 0);
        int dir = 1;
        n -= 2;
        while (n > 0) {
            int summ = 0;
            vector<int> next_dp(diff, 0);
            int j = 1;
            if (dir) {
                for (int i = diff-1; i >= 1; i--) {
                    summ = (summ + dp[i]) % MOD;
                    next_dp[i-1] = summ;
                }
            } else {
                for (int i = 0; i < diff-1; i++) {
                    summ = (summ + dp[i]) % MOD;
                    next_dp[i+1] = summ;
                }
            }
            dir ^= 1;
            dp = std::move(next_dp);
            n--;
        }

        int summ = 0;
        for (int i = 0; i < diff; i++) {
            summ = (summ + dp[i]) % MOD;
        }
        summ *= 2;
        summ %= MOD;
        return summ;
    }
};
