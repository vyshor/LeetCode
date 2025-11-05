class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        vector<vector<int>> ans;
        int n = arr.size();
        int minn = INT_MAX;
        for (int i = 1; i < n; i++) {
            int diff = arr[i] - arr[i-1];
            if (diff < minn) {
                minn = diff;
                ans = {{arr[i-1], arr[i]}};
            } else if (diff == minn) {
                ans.push_back({arr[i-1], arr[i]});
            }
        }
        return ans;
    }
};
