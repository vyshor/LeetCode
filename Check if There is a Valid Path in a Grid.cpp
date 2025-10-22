class Solution {
public:
    int N;

    bool bitequal(int bit, int mask) {
        return (bit & mask) == mask;
    }

    int keygen(int i, int j) {
        return i*N+j;
    }

    bool hasValidPath(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        N = n;
        // Up, right, down, left
        vector<int> mapping = {0, 0b0101, 0b1010, 0b0011, 0b0110, 0b1001, 0b1100};
        vector<int> visited(m*n, 0);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                grid[i][j] = mapping[grid[i][j]];
            }
        }

        vector<pair<int, int>> q;
        q.emplace_back(0, 0);

        while (q.size() > 0) {
            auto [i, j] = q.back();
            q.pop_back();
            if (i == (m-1) && j == (n-1)) return true;

            if (visited[keygen(i,j)]) continue;
            visited[keygen(i,j)] = 1;

            int bit = grid[i][j];
            // Up
            if (bitequal(bit, 0b1000) && i != 0 && !visited[keygen(i-1,j)] && bitequal(grid[i-1][j], 0b0010)) {
                q.emplace_back(i-1, j);
            }
            // Right
            if (bitequal(bit, 0b0100) && j != (n-1) && !visited[keygen(i,j+1)] && bitequal(grid[i][j+1], 0b0001)) {
                q.emplace_back(i, j+1);
            }
            // Down
            if (bitequal(bit, 0b0010) && i != (m-1) && !visited[keygen(i+1,j)] && bitequal(grid[i+1][j], 0b1000)) {
                q.emplace_back(i+1, j);
            }
            // Left
            if (bitequal(bit, 0b0001) && j != 0 && !visited[keygen(i,j-1)] && bitequal(grid[i][j-1], 0b0100)) {
                q.emplace_back(i, j-1);
            }
        }
        return false;
    }
};
