class Solution {
public:
    int maxDotProduct(vector<int>& nums1, vector<int>& nums2) {
        int n1 = nums1.size();
        int n2 = nums2.size();
        vector<vector<int>> dp(n1+1, vector<int>(n2+1, 0));
        int maxx{INT_MIN};
        for (int i{0}; i < n1; ++i) {
            for (int j{0}; j < n2; ++j) {
                maxx = max(maxx, nums1[i]*nums2[j]);
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + nums1[i]*nums2[j]);
                dp[i][j+1] = max(dp[i][j+1], dp[i][j]);
                dp[i+1][j] = max(dp[i+1][j], dp[i][j]);
            }
        }

        int maxx_minn{maxx};
        for (int i{0}; i < n1+1; ++i) {
            maxx = max(maxx, dp[i][n2]);
        }
        for (int j{0}; j < n2+1; ++j) {
            maxx = max(maxx, dp[n1][j]);
        }
        return (maxx == 0) ? maxx_minn : maxx;
    }
};
