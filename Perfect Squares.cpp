class Solution {
public:
    int numSquares(int n) {
        vector<uint16_t> arr;
        for (int i = 1; i < n+1; i++) {
            int sq = i*i;
            if (sq == n) return 1;
            if (sq > n) break;
            arr.push_back(sq);
        }

        vector<int> dp(n+1, n);
        dp.at(n) = 0;
        for (auto & num: arr) {
            for (int i = n; i > 0; i--) {
                if (i - num < 0) break;
                dp.at(i - num) = min(dp.at(i - num), dp.at(i)+1);
            }
        }

        return dp.at(0);
    }
};
