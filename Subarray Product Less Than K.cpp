class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        if (k == 0) return 0;
        int n = nums.size();
        double k2 = log((double) k);
        vector<double> arr(n, 0);
        for (int i = 0; i < n; i++) {
            arr[i] = log((double) nums[i]);
        }

        vector<double> dp(n+1, 0);
        double summ = 0;
        int count = 0;
        for (int i = 0; i < n; i++) {
            summ += arr[i];
            dp[i+1] = summ;
        }

        for (int i = 0; i < n; i++) {
            double remainder = k2 + dp[i];
            auto j = lower_bound(dp.begin(), dp.end(), remainder);
            int j2 = j - dp.begin();
            if (j2 < i+1) continue;
            count += j2-i-1;
        }

        return count;
    }
};

