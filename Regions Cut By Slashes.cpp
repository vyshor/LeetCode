class Solution {
public:
    int regionsBySlashes(vector<string>& grid) {
        int n = grid.size();
        int islands = (n*n) << 2;
        vector<int> parents(islands);
        for (int i = 0; i < islands; i++) parents[i] = i;
        function<int(int)> find;
        find = [&find, &parents] (int i) -> int {
            if (parents[i] == i) return i;

            int new_parent = find(parents[i]);
            parents[i] = new_parent;
            return new_parent;
        };

        auto uni = [&parents, &islands, &find] (int i, int j) {
            if (i < 0 || i >= parents.size() || j < 0 || j >= parents.size()) return;

            int parent_i = find(i);
            int parent_j = find(j);
            if (parent_i != parent_j) {
                islands--;
                parents[parent_j] = parent_i;
            }
        };

        auto get_pos = [&n] (int i, int j, int dir) {
            return ((i * n + j) << 2) + dir;
        };

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int pos = get_pos(i, j, 0);
                char c = grid[i][j];
                if (c == '/') {
                    uni(pos, get_pos(i, j, 3));
                    uni(pos, get_pos(i-1, j, 2));
                    if (j != 0)
                        uni(pos, get_pos(i, j-1, 1));

                    uni(pos+1, pos+2);
                    uni(pos+2, get_pos(i+1, j, 0));
                    if (j != n-1)
                        uni(pos+1, get_pos(i, j+1, 3));
                } else if (c == '\\') {
                    uni(pos, pos + 1);
                    uni(pos, get_pos(i-1, j, 2));
                    if (j != n-1)
                        uni(pos, get_pos(i, j+1, 3));

                    uni(pos+2, pos + 3);
                    uni(pos+2, get_pos(i+1, j, 0));
                    if (j != 0)
                        uni(pos+3, get_pos(i, j-1, 1));
                } else {
                    uni(pos, pos + 1);
                    uni(pos, pos + 2);
                    uni(pos, pos + 3);
                    uni(pos, get_pos(i-1, j, 2));
                    uni(pos, get_pos(i+1, j, 0));
                    if (j != 0)
                        uni(pos, get_pos(i, j-1, 1));
                    if (j != n-1)
                        uni(pos, get_pos(i, j+1, 3));
                }
            }
        }
        return islands;
    }
};