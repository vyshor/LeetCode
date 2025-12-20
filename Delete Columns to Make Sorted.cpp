class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int n = strs.size();
        int m = strs[0].size();
        int count{0};
        for (int i{0}; i < m; ++i) {
            char prev = strs[0][i];
            for (int j{1}; j < n; ++j) {
                if (strs[j][i] < prev) {
                    ++count;
                    break;
                }

                prev = strs[j][i];
            }
        }
        return count;
    }
};
