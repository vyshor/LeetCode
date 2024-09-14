class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        int xorr = 0, n = arr.size();
        vector<int> dp{0};
        for (int i = 0; i < n; i++) {
            xorr ^= arr[i];
            dp.push_back(xorr);
        }

        vector<int> ans;
        ans.reserve(queries.size());
        for (auto query: queries) {
            ans.push_back(dp[query[1]+1] ^ dp[query[0]]);
        }
        return ans;
    }
};
