class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int summ = 0;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            summ += nums[i];
        }

        if (target > 0 && summ < target) return 0;
        if (target < 0 && -summ > target) return 0;

        // -summ to target
        int m = summ+1+target;
        vector<int> dp(m, 0);
        dp[0] = 1;

        for (int i = 0; i < n; i++) {
            int num = 2*nums[i];

            for (int j = m-1; j >= num; j--) {
                dp[j] += dp[j-num];
            }
        }
        return dp[m-1];
    }
};
