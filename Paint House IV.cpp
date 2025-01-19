class Solution {
public:
    int64_t min2(int64_t a, int64_t b, int64_t c) {
        if (a <= b && a <= c) return a;
        if (b <= a && b <= c) return b;
        return c;
    }
    long long minCost(int n, vector<vector<int>>& cost) {
        int left = n / 2 - 1, right = n / 2;
        std::vector<int64_t> dp(6, 0);

        while (left >= 0) {
            std::vector<int64_t> new_dp(6);
            new_dp[0] = min2(dp[1], dp[2], dp[5]) + (int64_t)(cost[left][1] + cost[right][2]);
            new_dp[1] = min2(dp[0], dp[3], dp[4]) + (int64_t)(cost[right][1] + cost[left][2]);
            new_dp[2] = min2(dp[0], dp[3], dp[5]) + (int64_t)(cost[left][0] + cost[right][1]);
            new_dp[3] = min2(dp[1], dp[2], dp[4])  + (int64_t)(cost[right][0] + cost[left][1]);
            new_dp[4] = min2(dp[1], dp[3], dp[5])  + (int64_t)(cost[left][0] + cost[right][2]);
            new_dp[5] = min2(dp[0], dp[2], dp[4]) + (int64_t)(cost[right][0] + cost[left][2]);
            dp.swap(new_dp);
            left--;
            right++;
        }
        return std::min(min2(dp[0], dp[1], dp[2]), min2(dp[3], dp[4], dp[5]));
    }
};
