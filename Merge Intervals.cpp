class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> ans;
        sort(intervals.begin(), intervals.end());
        int n = intervals.size();
        int i = 1;
        int start = intervals[0][0], end = intervals[0][1];
        while (i < n) {
            int st = intervals[i][0], ed = intervals[i][1];
            if (st <= end) {
                end = max(end, ed);
            } else {
                ans.push_back({start, end});
                start = st;
                end = ed;
            }
            i++;
        }
        ans.push_back({start, end});
        return ans;
    }
};