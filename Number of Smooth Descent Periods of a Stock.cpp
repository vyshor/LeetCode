class Solution {
public:
    long long getDescentPeriods(vector<int>& prices) {
        long long ans{1};
        int n = prices.size();
        int prev = prices[0];
        int combo = 1;
        for (int i{1}; i < n; ++i) {
            if (prices[i] == prev-1) {
                ans += combo;
                ++combo;
            } else {
                combo = 1;
            }
            ++ans;
            prev = prices[i];
        }
        return ans;
    }
};