unordered_map<int, int> dp;

class Solution {
public:
    int recur(int i, int j) {
        int key = (i << 16) | j;
        if (dp.contains(key)) return dp[key];
        if (i >= j) return 0;

        int minn = (1 << 30);
        for (int k = i; k < j+1; k++) {
            // cout << i << " " << k << " " << j << endl;
            int cost = k + max(recur(k+1, j), recur(i, k-1));
            minn = min(minn, cost);
        }
        // cout << i << " " << j  << " cost: " << minn << endl;
        dp[key] = minn;
        return minn;
    }
    int getMoneyAmount(int n) {
        return recur(1, n);
    }
};
