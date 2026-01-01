class Solution {
public:
    int total;
    int row_;
    int col_;
    vector<int> parents;

    int flatten(int r, int c) {
        return r * col_ + c;
    }

    int latestDayToCross(int row, int col, vector<vector<int>>& cells) {
        total = row * col;
        row_ = row;
        col_ = col;

        int left_parent = total;
        int right_parent = total+1;

        parents = vector<int>(total+2);
        vector<int>is_block(total, 0);
        std::iota(parents.begin(), parents.end(), 0);

        function<int(int)> find;
        find = [&] (int i) -> int {
            // std::cout << i  << ' ' << parents[i] << '\n';
            if (parents[i] == i) return i;
            int new_parent = find(parents[i]);
            parents[i] = new_parent;
            return new_parent;
        };

        auto uni = [&] (int i, int j) -> bool {
            int parent_i = find(i);
            int parent_j = find(j);
            if (parent_i == parent_j) return false;
            if (parent_j == left_parent && parent_i == right_parent) return true;
            if (parent_i == left_parent && parent_j == right_parent) return true;
            if (parent_j == left_parent || parent_j == right_parent) {
                parents[parent_i] = parent_j;
            } else if (parent_i == left_parent || parent_i == right_parent) {
                parents[parent_j] = parent_i;
            } else {
                parents[parent_j] = parent_i;
            }
            return false;
        };

        vector<pair<int, int>> dirs{{
            {-1, -1},
            {-1,0},
            {0, -1},
            {-1, 1},
            {1, 1},
            {1, 0},
            {0, 1},
            {1, -1}
        }};

        int day{0};
        for (auto& cell: cells) {
            int i = cell[0]-1;
            int j = cell[1]-1;
            int idx = flatten(i, j);
            is_block[idx] = 1;

            if (j == 0) {
                bool block = uni(left_parent, idx);
                if (block) return day;
            } else if (j == col-1) {
                bool block = uni(right_parent, idx);
                if (block) return day;
            }

            for (auto [x,y]: dirs) {
                x += i;
                y += j;
                if (x < 0 || x >= row || y < 0 || y >= col) continue;

                int connect_idx = flatten(x, y);
                if (!is_block[connect_idx]) continue;

                bool block = uni(idx, connect_idx);
                // std::cout << idx << ", "  << connect_idx << " block:" <<block << '\n';
                if (block) return day;
            }

            ++day;
        }
        return 0;
    }
};
