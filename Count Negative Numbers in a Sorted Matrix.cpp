class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int count{0};
        int row_count = grid[0].size();
        for (auto& row: grid) {
            int idx = std::lower_bound(row.begin(), row.end(), -1, std::greater<>{}) - row.begin();
            // std::cout << "idx:" << idx << '\n';
            count += row_count - idx;
        }
        return count;
    }
};
