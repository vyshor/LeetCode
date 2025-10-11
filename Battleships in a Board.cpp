class Solution {
public:
    unordered_map<int, int> parents;
    int islands = 0;

    int find(int i) {
        if (!parents.contains(i)) {
            parents[i] = i;
            islands++;
            // cout << "i: " << i << endl;
            // cout << "Islands: "<< islands << endl;
            return i;
        }
        if (i == parents[i]) return i;
        int parent = find(parents[i]);
        parents[i] = parent;
        return parent;
    }

    void uni(int i, int j) {
        int parent_i = find(i);
        int parent_j = find(j);
        if (parent_i != parent_j) {
            parents[parent_j] = parent_i;
            islands--;
        }
    }

    int countBattleships(vector<vector<char>>& board) {
        int m = board.size();
        int n = board[0].size();
        vector<pair<int, int>> dirs {
            {1, 0},
            {-1, 0},
            {0, 1},
            {0, -1}
        };
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'X') {
                    // cout << "Found X " << i << " Y " << j << endl;
                    int origin_key = (i << 16) | j;
                    find(origin_key);
                    for (auto [x, y]: dirs) {
                        x += i;
                        y += j;
                        if (x < 0 || x >= m || y < 0 || y >= n) continue;
                        if (board[x][y] != 'X') continue;
                        int key = (x << 16) | y;
                        uni(origin_key, key);
                    }
                }
            }
        }
        return islands;
    }
};
