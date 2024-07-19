class Solution {
public:
    vector<int> luckyNumbers (vector<vector<int>>& matrix) {
        int n = matrix.size(), m = matrix[0].size();
        vector<int> rows(n, INT_MAX);
        vector<int> cols(m, 0);
        for (int i = 0; i< n; i++) {
            for (int j = 0; j < m; j++) {
                rows[i] = min(rows[i], matrix[i][j]);
                cols[j] = max(cols[j], matrix[i][j]);
            }
        }

        unordered_set<int> cols_set(cols.begin(), cols.end());
        vector<int> ans;
        for (int i = 0; i < n; i++) {
            if (cols_set.contains(rows[i])) ans.push_back(rows[i]);
        }
        return ans;
    }
};
