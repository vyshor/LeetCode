class Solution {
public:
    int minZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        int max_num = *max_element(nums.begin(), nums.end());
        vector<vector<int>> dp(n, vector<int>(max_num+1, 0));
        for (int i = 0; i < n; i++) {
            dp[i][nums[i]] = 1;
        }
        int k = 0;
        bool all_zero = true;
        for (int i = 0; i < n; i++) {
            if (dp[i][0] == 0) {
                all_zero = false;
                break;
            }
        }
        if (all_zero) return k;

        for (auto& query: queries) {
            k++;
            int l = query[0], r = query[1], val = query[2];
            for (int i = l; i < r+1; i++) {
                for (int j = 0; j < nums[i]+1-val; j++) {
                    dp[i][j] |= dp[i][j+val];
                }
            }

            all_zero = true;
            for (int i = 0; i < n; i++) {
                if (dp[i][0] == 0) {
                    all_zero = false;
                    break;
                }
            }
            if (all_zero) return k;
        }
        return -1;
    }
};