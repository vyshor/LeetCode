class Solution {
public:
    bool canReach(vector<int>& arr, int start) {
        int n = arr.size();
        vector<int> visited(n, 0);
        vector<int> q = {start};
        while (q.size() > 0) {
            int i = q.back();
            q.pop_back();
            if (visited[i]) continue;
            visited[i] = 1;

            int val = arr[i];
            if (val == 0) return true;
            if (i + val < n && !visited[i + val]) q.push_back(i + val);
            if (i - val >= 0 && !visited[i - val]) q.push_back(i - val);
        }
        return false;
    }
};
