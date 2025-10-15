class Solution {
public:
    int maxIncreasingSubarrays(vector<int>& nums) {
        int n = nums.size();
        int maxx_k = 0;
        vector<int> dp(n, 1);
        for (int i = 1; i < n; i++) {
            if (nums[i-1] < nums[i]) {
                dp[i] = dp[i-1]+1;
                maxx_k = max(maxx_k, dp[i]/2);
            }
            int current_k = dp[i];
            if (i-current_k >= 0 && dp[i-current_k] >= current_k) {
                maxx_k = max(maxx_k, current_k);
            }
        }
        return maxx_k;
    }
};
