class Solution {
public:
    long long maxMatrixSum(vector<vector<int>>& matrix) {
        long long summ{0};
        int minn = abs(matrix[0][0]);
        int sign{0};
        int n = matrix.size();
        int m = matrix[0].size();
        for (int i{0}; i < n; ++i) {
            for (int j{0}; j < m; ++j) {
                minn = min(minn, abs(matrix[i][j]));
                summ += abs(matrix[i][j]);
                sign ^= (matrix[i][j] < 0);
            }
        }
        if (sign) {
            return summ - 2*minn;
        }
        return summ;
    }
};