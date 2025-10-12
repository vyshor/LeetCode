class Solution {
public:
    vector<int> findRightInterval(vector<vector<int>>& intervals) {
        int n = intervals.size();
        vector<int> results(n, -1);
        vector<int> state(n, 0);
        vector<int> stack;
        vector<tuple<int, int, int>> q;
        q.reserve(n*2);

        int i = 0;
        for (auto& interval: intervals) {
            q.emplace_back(interval[0], 0, i);
            if (interval[0] == interval[1]) {
                results[i] = i;
            } else {
                q.emplace_back(interval[1], -1, i);
            }
            i++;
        }
        sort(q.begin(), q.end());
        i = 0;
        while (i < q.size()) {
            auto [t, _, idx] = q[i];
            state[idx] ^= 1;
            if (state[idx] == 0) {
                stack.push_back(idx);
            } else {
                while (stack.size() > 0) {
                    results[stack.back()] = idx;
                    stack.pop_back();
                }
            }
            i++;
        }
        return results;
    }
};
