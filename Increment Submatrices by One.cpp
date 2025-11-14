class Solution {
public:
    vector<vector<int>> rangeAddQueries(int n, vector<vector<int>>& queries) {
        int m = n+1;
        vector<vector<int>> diff(m, vector<int>(m, 0));
        for (auto& query: queries) {
            int row1 = query[0];
            int col1 = query[1];
            int row2 = query[2];
            int col2 = query[3];

            ++diff[row1][col1];
            ++diff[row2+1][col2+1];
            --diff[row1][col2+1];
            --diff[row2+1][col1];
        }

        vector<vector<int>> ans(n, vector<int>(n));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                bool valid_i = (i >= 1);
                bool valid_j = (j >= 1);
                ans[i][j] = diff[i][j] + (valid_i ? ans[i-1][j] : 0) + (valid_j ? ans[i][j-1] : 0) - (valid_i && valid_j ? ans[i-1][j-1] : 0);
            }
        }
        return ans;
    }
};
