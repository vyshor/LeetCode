class Solution {
public:
    unordered_map<int, int> dp{{0, 1}, {1, 1}, {2, 2}};
    int recur(int r) {
        if (dp.contains(r)) return dp[r];

        int summ = 0;
        for (int i = 0; i < r; i++) {
            summ += recur(i) * recur(r-1-i);
        }
        dp[r] = summ;
        return summ;
    }

    int numTrees(int n) {
        return recur(n);
    }
};