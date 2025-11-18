class Solution {
public:
    vector<int> bbits;
    vector<int> dp;

    int recur(int i) {
        if (i < 0) return 1;
        if (dp[i] != -1) return dp[i];

        if (i == 0) {
            dp[i] = bbits[0] == 0;
            return dp[i];
        }

        int valid = 0;
        if (bbits[i] == 0) {
            valid |= recur(i-1);
            if (bbits[i-1] == 1) {
                valid |= recur(i-2);
            }
        } else if (bbits[i-1] == 1) {
            valid |= recur(i-2);
        }
        dp[i] = valid;
        return dp[i];
    }

    bool isOneBitCharacter(vector<int>& bits) {
        int n = bits.size();
        if (n == 1) return true;

        dp = vector<int>(n, -1);
        bbits = std::move(bits);
        return recur(n-2);
    }
};
