class Solution {
public:
    long long maxPoints(vector<vector<int>>& points) {
        int n = points.size(), m = points[0].size();
        vector<int64_t> prev_results(m);

        for (int j = 0; j < m; j++) {
            prev_results[j] = (int64_t) points[0][j];
        }

        for (int i = 0; i < n-1; i++) {
            int64_t maxx = 0;
            vector<int64_t> dp(m, 0);
            for (int j = 0; j < m; j++) {
                maxx = max(maxx-1, prev_results[j]);
                dp[j] = maxx;
            }

            maxx = 0;
            for (int j = m-1; j >= 0; j--) {
                maxx = max(maxx-1, prev_results[j]);
                prev_results[j] = points[i+1][j] + max(dp[j], maxx);
            }
        }
        int64_t ans = 0;
        for (int64_t i: prev_results) {
            ans = max(ans, i);
        }
        return ans;
    }
};
