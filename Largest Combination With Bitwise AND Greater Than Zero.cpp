class Solution {
public:
    int largestCombination(vector<int>& candidates) {
        vector<int> dp;
        auto countBits = [&dp] (int num) {
            int i = 0;
            while (num > 0) {
                if (i == dp.size()) dp.push_back(0);
                dp[i] += num % 2;
                i++;
                num >>= 1;
            }
        };

        for (int num: candidates) countBits(num);
        return *max_element(dp.begin(), dp.end());
    }
};
