class Solution {
public:
    double new21Game(int n, int k, int maxPts) {
        if (n == 0 || k == 0 || k+maxPts-1 <= n) return 1.;

        int m = maxPts+2;
        vector<double> dp(m, 0.);
        dp[0] = 1.0;
        dp[1] = -1.0;

        double change = 0.0;
        for (int i = 0; i < k; i++) {
            // Diff array concept
            change += dp[i % m];
            double chance = change / double(maxPts);
            dp[i % m] = 0.;
            dp[(i+maxPts+1) % m] -= chance;
            dp[(i+1) % m] += chance;
        }

        double ans = 0.;
        for (int i = k; i < n+1; i++) {
            change += dp[i % m];
            ans += change;
        }
        return ans;
    }
};