class Solution {
public:
    double new21Game(int n, int k, int maxPts) {
        if (n == 0 || k == 0 || k+maxPts-1 <= n) return 1.;

        int m = maxPts+2;
        vector<double> dp(m, 0.);

        double curr = 1.0, change = 0.0;
        for (int i = 0; i < k; i++) {
            // Diff array concept
            // cout << "i=" << i << " dp[i]= " << dp[i % m] << " curr=" << curr  << " change=" << change << endl;
            change += dp[i % m];
            curr += change;
            double chance = curr / double(maxPts);
            curr = 0.;
            dp[i % m] = 0.;
            dp[(i+maxPts+1) % m] -= chance;
            dp[(i+1) % m] += chance;
        }

        double ans = 0.;
        curr = change;
        // cout << "Change=" << change << endl;
        for (int i = k; i < n+1; i++) {
            // cout << "i=" << i << " dp[i]= " << dp[i % m] << " ans=" << ans << endl;
            curr += dp[i % m];
            ans += curr;
        }
        return ans;
    }
};
