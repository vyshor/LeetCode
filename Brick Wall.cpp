class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        uint64_t wall_length = 0;
        int m = wall.size();
        for (auto length: wall[0]) {
            wall_length += uint64_t(length);
        }

        vector<uint64_t> pos;
        unordered_map<uint64_t, int> diff;

        for (int j = 0; j < m; j++) {
            uint64_t summ = 0;

            for (auto length: wall[j]) {
                if (!diff.contains(summ)) {
                    pos.push_back(summ);
                }

                if (!diff.contains(summ+1)) {
                    pos.push_back(summ+1);
                }
                diff[summ+1]++;
                summ += length;

                if (!diff.contains(summ)) {
                    pos.push_back(summ);
                }
                diff[summ]--;
            }
        }

        sort(pos.begin(), pos.end());
        int minn = m;
        int summ = 0;
        // cout << "Diff: ";
        for (uint64_t i: pos) {
            summ += diff[i];
            // cout << diff[i] << " ";
            if (i != 0 && i != wall_length) {
                minn = min(minn, summ);
            }
        }
        // cout << endl;
        return minn;
    }
};
