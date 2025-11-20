class Solution {
public:
    int intersectionSizeTwo(vector<vector<int>>& intervals) {
        int n = intervals.size();
        vector<int> counter(n);
        vector<pair<int, int>> starters;
        vector<tuple<int, int, int>> required;

        starters.reserve(n);
        required.reserve(n*2);

        for (int i{0}; i < n; ++i) {
            int start = intervals[i][0];
            int end = intervals[i][1];


            starters.emplace_back(start, i);
            required.emplace_back(end-1, 1, i);
            required.emplace_back(end, 2, i);
        }

        sort(starters.begin(), starters.end());
        sort(required.begin(), required.end());

        int ans{0};
        vector<int> opens;
        int i{0}, j{0};
        while (j < 2*n) {
            while (i < n && starters[i].first <= get<0>(required[j])) {
                opens.push_back(starters[i].second);
                ++i;
            }

            int target = get<1>(required[j]);
            int idx = get<2>(required[j]);
            if (counter[idx] < target) {
                ++ans;
                vector<int> new_opens;
                new_opens.reserve(opens.size());
                for (int idx2: opens) {
                    ++counter[idx2];
                    if (counter[idx2] < 2) new_opens.push_back(idx2);
                }
                opens.swap(new_opens);
            }
            ++j;
        }
        return ans;
    }
};
