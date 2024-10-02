class Solution {
public:
    bool canArrange(vector<int>& arr, int k) {
        vector<int> dp(k, 0);
        for (int num: arr) {
            if (num < 0) {
                num += ((-num / k) + 1)*k;
            }
            dp[num % k]++;
        }

        if (dp[0] % 2 == 1) return false;

        int i = 1, j = dp.size() - 1;
        while (i < j) {
            if (dp[i] != dp[j]) return false;
            i++;
            j--;
        }

        if (i == j) return (dp[i] % 2 == 0);
        return true;
    }
};
