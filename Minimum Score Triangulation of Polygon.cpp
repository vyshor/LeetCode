class Solution {
public:
    unordered_map<int, int> dp;
    vector<int> vals;

    int recur(int i, int j) {
        int key = (i << 16) | j;
        if (dp.contains(key)) return dp[key];
        if (i+1 == j) return 0;

        int minn = 1 << 30;
        for (int k = i+1; k < j; k++) {
            int left = recur(i, k);
            int triangle = vals[i] * vals[j] * vals[k];
            int right = recur(k, j);
            if (left > minn || right > minn || triangle > minn) continue;
            int summ = left + triangle + right;
            minn = min(minn, summ);
        }
        dp[key] = minn;
        return minn;
    }

    int minScoreTriangulation(vector<int>& values) {
        int n = values.size();
        vals = values;
        return recur(0, n-1);
    }
};
