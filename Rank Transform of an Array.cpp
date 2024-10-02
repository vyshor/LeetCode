class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        if (arr.size() == 0) return {};
        int n = arr.size();
        vector<pair<int, int>> dp;
        int i = 0;
        for (int num: arr) {
            dp.emplace_back(num, i++);
        }

        sort(dp.begin(), dp.end());
        vector<int> ans(n);
        int rank = 1, prev = dp[0].first;
        for (auto [num, i]: dp) {
            if (num != prev) rank++;
            ans[i] = rank;
            prev = num;
        }
        return ans;
    }
};