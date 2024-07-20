class Solution {
public:
    vector<vector<int>> restoreMatrix(vector<int>& rowSum, vector<int>& colSum) {
        int n = rowSum.size(), m = colSum.size();
        vector<vector<int>> matrix;
        matrix.reserve(n);
        for (int i = 0; i < n; i++) {
            matrix.emplace_back(m, 0);
        }
        int i = 0, j = 0;
        while (i < n && j < m) {
            matrix[i][j] = min(rowSum[i], colSum[j]);
            rowSum[i] -= matrix[i][j];
            colSum[j] -= matrix[i][j];
            while (i < n && rowSum[i] == 0) i++;
            while (j < m && colSum[j] == 0) j++;
        }
        return matrix;
    }
};
