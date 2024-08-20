class Solution {
public:
    int stoneGameII(vector<int>& piles) {
        map<int64_t, int> dp;
        int n = piles.size();
        auto key = [] (int i, int turn, int m) -> int64_t {
            int64_t k = m;
            k <<= 1;
            k |= turn;
            k <<= 10;
            k |= i;
            return k;
        };

        function<int(int, int, int)> maximise;
        maximise = [&key, &maximise, &n, &piles, &dp] (int i, int turn, int m) -> int {
            if (i == n) return 0;

            int64_t k = key(i, turn, m);
            if (dp.count(k)) return dp[k];

            int maxx = INT_MIN;
            int summ = 0;
            for (int j = 0; j < m*2; j++) {
                if (i+j >= n) break;

                summ += piles[i+j];
                maxx = max(maxx, summ - maximise(i+j+1, 1 ^ turn, max(m, j+1)));
            }
            dp[k] = maxx;
            return maxx;
        };

        int total = 0;
        for (int pile: piles) {
            total += pile;
        }
        int max_diff = maximise(0, 1, 1);
        if (max_diff > 0) return (total - max_diff) / 2 + max_diff;
        return (total + max_diff) / 2;
    }
};
