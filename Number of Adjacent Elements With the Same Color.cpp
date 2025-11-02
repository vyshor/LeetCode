class Solution {
public:
    vector<int> colorTheArray(int n, vector<vector<int>>& queries) {
        vector<int> colors(n, 0);
        vector<int> ans;
        ans.reserve(queries.size());

        int pairs = 0;
        for (auto& query: queries) {
            int idx = query[0];
            int color = query[1];

            if (idx > 0) {
                pairs -= ((colors[idx-1] ^ colors[idx]) == 0) * (colors[idx] != 0);
            }
            if (idx < n-1) {
                pairs -= ((colors[idx] ^ colors[idx+1]) == 0) * (colors[idx] != 0);
            }
            colors[idx] = color;
            if (idx > 0) {
                pairs += ((colors[idx-1] ^ colors[idx]) == 0) * (colors[idx] != 0);
            }
            if (idx < n-1) {
                pairs += ((colors[idx] ^ colors[idx+1]) == 0) * (colors[idx] != 0);
            }
            ans.push_back(pairs);
        }
        return ans;
    }
};
