class Solution {
public:
    int maxTotalReward(vector<int>& rewardValues) {
        sort(rewardValues.begin(), rewardValues.end());
        int max_val = rewardValues.back()*2-1;
        bitset<100'001> dp{}, mask{};
        dp[0] = 1;

        int n = rewardValues.size();
        unordered_set<int> seen;

        int prev = 0;
        for (int i = 0; i < n; i++) {
            int reward = rewardValues[i];
            if (seen.contains(reward)) continue;
            seen.insert(reward);

            while (prev < reward) {
                mask.set(prev);
                prev++;
            }

            dp |= ((dp & mask) << reward);
            prev = reward;
        }

        for (int i = max_val; i >= 1; i--) {
            if (dp[i]) return i;
        }
        return 0;
    }
};