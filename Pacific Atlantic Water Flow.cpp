class Solution {
public:
    unordered_map<int, int> oceans;
    vector<vector<int>> hs;
    int m;
    int n;

    void recur(int i, int j, int state = 0) {
        int key = (i << 16) | j;
        if (oceans.contains(key)) {
            if ((oceans[key] & state) > 0) return;
        }
        oceans[key] |= state;

        vector<pair<int, int>> dirs {
            {1, 0},
            {-1, 0},
            {0, 1},
            {0, -1}
        };

        for (auto [x, y]: dirs) {
            x += i;
            y += j;
            if (x >= m || x < 0 || y >= n || y < 0) continue;
            if (hs[x][y] < hs[i][j]) continue;

            recur(x, y, state);
        }
    }
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        m = heights.size();
        n = heights[0].size();
        hs = std::move(heights);

        std::vector<pair<int, int>> q;

        for (int i = 0; i < m; i++) {
            recur(i, 0, 0b01);
            recur(i, n-1, 0b10);
        }

        for (int j = 0; j < n; j++) {
            recur(0, j, 0b01);
            recur(m-1, j, 0b10);
        }

        vector<vector<int>> ans;
        for (auto [k, mask]: oceans) {
            if (mask == 0b11) {
                int j = ((1 << 16) - 1) & k;
                int i = k >> 16;
                // cout << i << "," << j << "  " << mask << endl;
                ans.push_back({i, j});
            }
        }
        return ans;
    }
};
