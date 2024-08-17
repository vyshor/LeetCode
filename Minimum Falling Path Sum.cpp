class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        int n = matrix.size(), m = matrix[0].size();
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int cost = matrix[i-1][j];
                if (j > 0) cost = min(cost, matrix[i-1][j-1]);
                if (j < m-1) cost = min(cost, matrix[i-1][j+1]);
                matrix[i][j] += cost;
            }
        }
        return *min_element(matrix[n-1].begin(), matrix[n-1].end());
    }
};
