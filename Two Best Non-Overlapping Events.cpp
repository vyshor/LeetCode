class Solution {
public:
    int maxTwoEvents(vector<vector<int>>& events) {
        vector<pair<int, int>> start_q, end_q;
        int n = events.size();
        for (int i{0}; i < n; ++i) {
            start_q.emplace_back(events[i][0], i);
            end_q.emplace_back(events[i][1], i);
        }
        std::sort(start_q.begin(), start_q.end());
        std::sort(end_q.begin(), end_q.end());
        int i{0};
        int j{0};
        int maxx1{0};
        int maxx{0};
        while (i < n) {
            while (end_q[j].first < start_q[i].first) {
                int idx = end_q[j].second;
                maxx1 = max(maxx1, events[idx][2]);
                ++j;
            }

            int idx2 = start_q[i].second;
            maxx = max(maxx, maxx1 + events[idx2][2]);
            ++i;
        }
        return maxx;
    }
};
