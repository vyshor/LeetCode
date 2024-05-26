class Solution {
public:
    int checkRecord(int n) {

    function<int64_t(int64_t)> mod = [] (int64_t num) -> int64_t {
        const int64_t MOD = 1000000007;
        return num % MOD;
    };

    int64_t dp_01 = 1, dp_02 = 0, dp_03 = 1, dp_10 = 1, dp_11 = 0, dp_12 = 0, dp_13 = 0;

    for (int i = 1; i < n; i++) {
        int64_t dp_01_ = dp_03, dp_02_ = dp_01, dp_03_ = mod(dp_01+dp_02+dp_03);
        int64_t dp_10_ = mod(dp_01+dp_02+dp_03), dp_11_ = mod(dp_10+dp_13), dp_12_ = dp_11, dp_13_ = mod(dp_10+dp_11+dp_12+dp_13);

        dp_01 = dp_01_;
        dp_02 = dp_02_;
        dp_03 = dp_03_;
        dp_10 = dp_10_;
        dp_11 = dp_11_;
        dp_12 = dp_12_;
        dp_13 = dp_13_;
    }

    int64_t total = mod(dp_01 + dp_02 + dp_03 + dp_10 + dp_11 + dp_12 + dp_13);
    return (int) total;
    }
};

//class Solution {
//public:
//    int checkRecord(int n) {
//
//    function<int64_t(int64_t)> mod = [&] (int64_t num) -> int64_t {
//        const int64_t MOD = 1000000007;
//        return num % MOD;
//    };
//
//    vector<vector<int64_t>> dp {
//        {0, 1, 0, 1},
//        {1, 0, 0, 0},
//    };
//
//    for (int i = 1; i < n; i++) {
//        vector<vector<int64_t>> new_dp{
//            {0, dp[0][3], dp[0][1], mod(dp[0][1]+dp[0][2]+dp[0][3])},
//            {mod(dp[0][1]+dp[0][2]+dp[0][3]), mod(dp[1][0]+dp[1][3]), dp[1][1], mod(dp[1][0]+dp[1][1]+dp[1][2]+dp[1][3])},
//        };
//        swap(dp, new_dp);
//    }
//
//    int64_t total = 0;
//    for (int i = 0; i < 2; i++) {
//        for (int j = 0; j < 4; j++) {
//            total += dp[i][j];
//            total = mod(total);
//        }
//    }
//    return (int) total;
//    }
//};
