class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        int low = newInterval.at(0), high = newInterval.at(1);
        bool merged = false;

        vector<vector<int>> ans;
        ans.reserve(intervals.size());
        for (auto& interval: intervals) {
            if (interval.at(1) < low) {
                ans.push_back(move(interval));
                continue;
            }

            if (interval.at(0) > high) {
                if (!merged) {
                    vector<int> a{low, high};
                    ans.push_back(a);
                    merged = true;
                }
                ans.push_back(move(interval));
            }

            if (!merged) {
                high = max(high, interval.at(1));
                low = min(low, interval.at(0));
            }
        }

        if (!merged) {
            vector<int> a{low, high};
            ans.push_back(a);
        }

        return ans;
    }
};
