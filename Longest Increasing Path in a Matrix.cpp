class Solution {
public:
    vector<vector<int>> mat;
    unordered_map<int, int> visited;
    int m;
    int n;

    int recur(int i, int j) {
        int key = (i << 16) | j;
        if (visited.contains(key)) return visited[key];

        vector<pair<int, int>> dirs = {
            {1, 0},
            {-1, 0},
            {0, 1},
            {0, -1}
        };

        int maxx = 1;
        for (auto [x, y]: dirs) {
            x += i;
            y += j;
            if (x < 0 || x >= m || y < 0 || y >= n) continue;
            if (mat[i][j] > mat[x][y]) {
                maxx = max(maxx, 1+recur(x, y));
            }
        }
        visited[key] = maxx;
        return maxx;
    }

    int longestIncreasingPath(vector<vector<int>>& matrix) {
        m = matrix.size();
        n = matrix[0].size();
        mat = std::move(matrix);
        int maxx = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                maxx = max(maxx, recur(i, j));
            }
        }
        return maxx;
    }
};
