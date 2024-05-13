class Solution {
public:
    int matrixScore(vector<vector<int>>& grid) {
    int n = grid.size(), m = grid[0].size();
    for (int i = 0; i < n; i++) {
        if (grid[i][0] == 0) {
            for (int j = 0; j < m; j++) {
                grid[i][j] ^= 1;
            }
        }
    }

    int count = n * ( 1 << (m-1));
    for (int j = 1; j < m; j++) {
        int current_count = 0;
        for (int i = 0; i < n; i++) {
            current_count += grid[i][j];
        }
        count += (1 << (m-1-j)) * max(current_count, n-current_count);
    }
    return count;
    }
};
