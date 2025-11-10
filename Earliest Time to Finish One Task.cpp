class Solution {
public:
    int earliestTime(vector<vector<int>>& tasks) {
        int minn = tasks[0][0] + tasks[0][1];
        int n = tasks.size();
        for (int i = 1; i < n; ++i) {
            minn = min(minn, tasks[i][0] + tasks[i][1]);
        }
        return minn;
    }
};
