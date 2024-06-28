class Solution {
public:
    long long maximumImportance(int n, vector<vector<int>>& roads) {
        vector<int64_t> arr(n, 0);
        for (vector<int>& road: roads) {
            arr[road[0]]++;
            arr[road[1]]++;
        }

        sort(arr.begin(), arr.end());
        int64_t summ = 0;
        int64_t n2 = n;
        while (n2 > 0) {
            summ += n2 * arr[--n2];
        }
        return summ;
    }
};
