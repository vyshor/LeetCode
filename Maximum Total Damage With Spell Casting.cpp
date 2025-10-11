class Solution {
public:
    long long maximumTotalDamage(vector<int>& power) {
        unordered_map<int, int> counter;
        vector<int> arr;
        for (int p: power) {
            if (!counter.contains(p)) arr.push_back(p);
            counter[p]++;
        }
        sort(arr.begin(), arr.end());

        int n = arr.size();
        arr.push_back(INT_MAX);

        vector<int64_t> dp(n+1, 0);

        int right = 0;
        for (int i = 0; i < n; i++) {
            int val = arr[i];
            int count = counter[val];
            int64_t summ = int64_t(val) * int64_t(count);

            // The case where you cast current spell
            while (right < n && arr[right] <= val+2) {
                right++;
            }
            dp[right] = max(dp[right], dp[i] + summ);

            // Case don't cast current spell
            dp[i+1] = max(dp[i+1], dp[i]);
        }

        // cout << "Val: ";
        // for (int i = 0; i < n; i++) {
        //     cout << arr[i] << " ";
        // }
        // cout << endl;
        // cout << "Dp: ";
        // for (int i = 0; i < n+1; i++) {
        //     cout << dp[i] << " ";
        // }
        // cout << endl;

        return dp[n];
    }
};
