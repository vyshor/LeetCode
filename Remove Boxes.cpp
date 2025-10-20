class Solution {
public:
    unordered_map<int, int> dp;
    vector<int> nxt;

    int recur(int i, int j, int count) {
        if (i > j) return 0;
        if (i == j) return count*count;

        int key = (i << 14) | (j << 7) | count;
        if (dp.contains(key)) return dp[key];

        int nxt_idx = nxt[i];

        // Base case, just consume current count val
        int summ = count*count+recur(i+1, j, 1);

        // Combine with next common
        while (nxt_idx <= j) {
            summ = max(summ, recur(i+1, nxt_idx-1, 1) + recur(nxt_idx, j, count+1));
            nxt_idx = nxt[nxt_idx];
        }

        dp[key] = summ;
        return dp[key];
    }

    int removeBoxes(vector<int>& boxes) {
        int n = boxes.size();
        nxt = vector<int>(n, n);
        vector<int> prev(101, -1);
        for (int i = 0; i < n; i++) {
            int num = boxes[i];
            if (prev[num] != -1) {
                nxt[prev[num]] = i;
            }
            prev[num] = i;
        }

        // cout << "Nxt_idx ";
        // for (int i = 0; i < n; i++) {
        //     cout << nxt[i] << " ";
        // }
        // cout << endl;

        return recur(0, n-1, 1);
    }
};
