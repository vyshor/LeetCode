class Solution {
public:
    int maxMoves(vector<vector<int>>& grid) {
        unordered_map<int, int> dp;
        int n = grid.size(), m = grid[0].size();
        function<int(int, int)> recur;
        recur = [&recur, &dp, &n, &m, &grid] (int i, int j) -> int {
            int key = (i << 10 | j);
            if (dp.contains(key)) return dp[key];
            if (j == m) return 0;
            if (j+1 == m) return 1;
            int moves = 0, val = grid[i][j];
            if (grid[i][j+1] > val) moves = max(moves, recur(i, j+1));
            if (i-1 >= 0 && grid[i-1][j+1] > val) moves = max(moves, recur(i-1, j+1));
            if (i+1 < n && grid[i+1][j+1] > val) moves = max(moves, recur(i+1, j+1));
            dp[key] = moves+1;
            return moves+1;
        };

        int maxx = 0;
        for (int i = 0; i < n; i++) {
            maxx = max(maxx, recur(i, 0));
        }
        return maxx-1;
    }
};
