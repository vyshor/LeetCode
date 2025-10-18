class Solution {
public:
    unordered_map<int64_t, int> dp;
    int64_t K;

    int recur(int64_t level, int64_t jump, int64_t used_back) {
        // cout << "level=" << level << " jump=" << jump << " used_back=" << used_back << endl;
        if (level > K+1) return 0;
        int64_t key = (level << 32) | (jump << 1) | used_back;
        if (dp.contains(key)) return dp[key];

        dp[key] = (level == K) + recur(level+(1 << jump), jump+1, 0);
        if (!used_back && (level > 0)) {
            dp[key] += recur(level-1, jump, 1);
        }

        return dp[key];
    }

    int waysToReachStair(int k) {
        K = k;
        return recur(1, 0, 0);
    }
};
