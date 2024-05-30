class Solution {
public:
    int countTriplets(vector<int>& arr) {
        int n = arr.size(), count = 0;
        unordered_map<int64_t, int> dp;
        for (int64_t i = 0; i < n; i++) {
            int64_t current_xor = 0;
            for (int64_t j = i; j < n;j++) {
                current_xor ^= (int64_t) arr[j];
                int64_t key1 = ((i-1) << 32) | current_xor, key2 = ((j) << 32) | current_xor;
                if (dp.contains(key1)) count += dp[key1];
                if (!dp.contains(key2)) dp[key2] = 1;
                else dp[key2]++;
            }
        }
        return count;
    }
};
