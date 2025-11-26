class Solution {
public:
    long long maxSubarraySum(vector<int>& nums, int k) {
        int n = nums.size();
        vector<long long> prefix(n+1, 0);
        for (int i{0}; i < n; ++i) {
            prefix[i+1] = prefix[i] + static_cast<long long>(nums[i]);
        }

        vector<long long> maxx(k, LLONG_MIN);
        vector<long long> dp(k, LLONG_MIN);
        for (int i{0}; i < k; ++i) {
            if (k+i > n) break;
            dp[i] = prefix[k+i] - prefix[i];
            maxx[i] = dp[i];
        }

        for (int i{k}; i <= n-k; ++i) {
            long long interval = prefix[i+k]-prefix[i];
            dp[i % k] = max(interval, dp[i % k] + interval);
            maxx[i % k] = max(maxx[i % k], dp[i % k]);
        }

        // for (int i{0}; i < k; ++i) {
        //     cout << maxx[i] << " ";
        // }

        return *max_element(maxx.begin(), maxx.end());
    }
};
