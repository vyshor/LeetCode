class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int n = strs.size();
        int m = strs[0].size();

        vector<stringstream> ss(n);
        int count{0};
        for (int i{0}; i < m; ++i) {
            int must_del = 0;
            for (int j{1}; j < n; ++j) {
                must_del |= ((ss[j].str() + strs[j][i]) < (ss[j-1].str() + strs[j-1][i]));
            }
            count += must_del;
            if (!must_del) {
                for (int j{0}; j < n; ++j) {
                    ss[j] << strs[j][i];
                }
            }
        }
        return count;
    }
};
