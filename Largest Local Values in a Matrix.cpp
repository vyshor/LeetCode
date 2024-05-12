class Solution {
public:
    vector<vector<int>> largestLocal(vector<vector<int>>& grid) {
        int n =grid.size();
        vector<vector<int>> new_grid;
        for (int i = 0;i < n-2; i++) {
            new_grid.emplace_back(n-2, 0);
        }

        for (int i =0; i<n; i++) {
            for (int j = 0; j < n; j++) {
                for (int i2 = i-1; i2 < i+2; i2++) {
                    for (int j2= j-1; j2 < j+2; j2++) {
                        if (1 <= i2 && i2 < n-1 && 1 <= j2 && j2 < n-1)
                            new_grid[i2-1][j2-1] = max(new_grid[i2-1][j2-1], grid[i][j]);
                    }
                }
            }
        }

        return new_grid;
    }
};

