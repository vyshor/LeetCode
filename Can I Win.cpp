unordered_map<int, bool> dp;

class Solution {
public:
    bool recur(int state, int total) {
        int key = (state << 10) | total;
        if (dp.contains(key)) return dp[key];

        int i = 0;
        int original_state = state;
        while (state > 0) {
            if (state & 1) {
                if ((total - i - 1) <= 0) {
                    dp[key] = true;
                    return true;
                } else {
                    bool otherCanWin = recur(original_state ^ (1 << i), total - i - 1);
                    if (!otherCanWin) {
                        dp[key] = true;
                        return true;
                    }
                }
            }

            state >>= 1;
            i++;
        }
        dp[key] = false;
        return false;
    };

    bool canIWin(int maxChoosableInteger, int desiredTotal) {
        if (maxChoosableInteger * (maxChoosableInteger + 1) / 2 < desiredTotal) return false;
        return recur((1 << maxChoosableInteger) - 1, desiredTotal);
    }
};