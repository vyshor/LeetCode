class Solution {
public:
    vector<vector<int>> spiralMatrixIII(int rows, int cols, int rStart, int cStart) {
        int total = rows * cols - 1;
        vector<int> movement{1,1,2,2};
        int direction = 0;
        vector<pair<int, int>> multiplier{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        vector<vector<int>> ans{{rStart, cStart}};
        while (total) {
            auto [move_x, move_y] = multiplier[direction];
            for (int i = 1; i <= movement[direction]; i++) {
                rStart += move_x;
                cStart += move_y;

                if (0 <= rStart && rStart < rows && 0 <= cStart && cStart < cols) {
                    ans.push_back({rStart, cStart});
                    total--;
                }
            }

            movement[direction] += 2;
            direction++;
            direction %= 4;
        }
        return ans;
    }
};
