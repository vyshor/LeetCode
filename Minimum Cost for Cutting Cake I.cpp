class Solution {
public:
    int M;
    int N;
    vector<int> dp;
    vector<int> hcut;
    vector<int> vcut;

    int minCost(int i1, int j1, int i2, int j2) {
        constexpr int offset = 400;
        int key = ((i1 * N + j1) * offset) + (i2 * N + j2);
        if (dp[key] != -1) return dp[key];

        if (i1 == i2 && j1 == j2) {
            dp[key] = 0;
            return 0;
        }

        int minn = INT_MAX;
        for (int i{i1}; i < i2; ++i) {
            minn = min(minn, hcut[i] + minCost(i1, j1, i, j2) + minCost(i+1, j1, i2, j2));
        }

        for (int j{j1}; j < j2; ++j) {
            minn = min(minn, vcut[j] + minCost(i1, j1, i2, j) + minCost(i1, j+1, i2, j2));
        }
        dp[key] = minn;
        return dp[key];
    }

    int minimumCost(int m, int n, vector<int>& horizontalCut, vector<int>& verticalCut) {
        M = m;
        N = n;
        dp = vector<int>(400*400, -1);
        hcut = std::move(horizontalCut);
        vcut = std::move(verticalCut);
        return minCost(0, 0, m-1, n-1);
    }
};
