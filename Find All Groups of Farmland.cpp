class Solution {
public:
    vector<vector<int>> findFarmland(vector<vector<int>>& land) {
        int n = land.size(), m = land[0].size();
        vector<vector<int>> ans;
        unordered_map<int, int> jumps;

        int i = 0;
        while (i < n) {
            int j = 0;
            while (j < m) {
                if (land[i][j]) {
                    if (jumps.contains((i << 10) | j)) {
                        j = jumps[((i << 10) | j)];
                        continue;
                    } else {
                        int x = i;
                        int y = j;
                        while (y+1 < m && land[x][y+1]) y++;
                        while (x+1<n && land[x+1][y]) x++;
                        ans.push_back({i, j, x, y});
                        for (int k = i+1; k < x+1; k++) jumps[(k<<10 | j)] = y+1;
                        j = y;
                    }
                }
                j++;
            }
            i++;
        }
        return ans;
    }
};
