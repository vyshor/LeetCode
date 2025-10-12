class Solution {
public:
    int arrangeCoins(int n) {
        int64_t sq = sqrt(double(n));
        int valid_n = 1;
        for (int64_t i = sq; i < n; i++) {
            int64_t product = i * (i+1) / 2;
            if (product <= n) valid_n = i;
            else return valid_n;
        }
        return valid_n;
    }
};
