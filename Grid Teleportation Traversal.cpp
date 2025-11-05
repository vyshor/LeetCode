class Solution {
public:
    int minMoves(vector<string>& matrix) {
        unordered_set<int64_t> visited;
        int m = matrix.size();
        int n = matrix[0].size();

        int portal_bits = 0;
        vector<vector<pair<int, int>>> portals(26);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] >= 65) {
                    int idx = matrix[i][j]-65;
                    portals[idx].emplace_back(i, j);
                }
            }
        }

        deque<pair<int, int>> q;
        q.emplace_back(0, 0);

        while (q.size() > 0) {
            int cost = q.front().first;
            int pos = q.front().second;
            q.pop_front();

            if (visited.contains(pos)) continue;
            visited.insert(pos);

            int i = ((1 << 10) - 1) & pos;
            int j = (pos >> 10);

            if (i == m-1 && j == n-1) return cost;

            // cout << i << " " << j << endl;

            int ch = matrix[i][j];
            // Can use portal
            if (ch >= 65) {
                int offset = ch-65;
                int mask = (1 << offset);
                if ((portal_bits & mask) == 0) {
                    portal_bits |= mask;
                    for (auto [x, y]: portals[offset]) {
                        if (x == i && y == j) continue;

                        int new_pos = x | (y << 10);
                        if (visited.contains(new_pos)) continue;
                        q.emplace_front(cost, new_pos);
                    }
                }
            }

            vector<pair<int, int>> moves = {
                {1, 0},
                {-1, 0},
                {0, 1},
                {0, -1}
            };

            for (auto [x, y]: moves) {
                x += i;
                y += j;
                if (x < 0 || x >= m || y < 0 || y >= n || matrix[x][y] == '#') continue;
                int new_pos = x | (y << 10);
                if (visited.contains(new_pos)) continue;

                q.emplace_back(cost+1, new_pos);
            }
        }

        return -1;
    }
};
