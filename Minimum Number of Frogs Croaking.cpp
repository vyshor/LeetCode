class Solution {
public:
    int minNumberOfFrogs(string croakOfFrogs) {
        unordered_map<char, int> mapping = {
            {'c', 0},
            {'r', 1},
            {'o', 2},
            {'a', 3},
            {'k', 4}
        };

        vector<int> dp(5, 0);
        int maxx = 0;
        int count = 0;
        for (char ch: croakOfFrogs) {
            int i = mapping[ch];
            if (i == 0) {
                dp[i]++;
                count++;
                maxx = max(maxx, count);
            } else {
                if (dp[i-1] == 0) return -1;
                dp[i-1]--;
                dp[i]++;

                if (i == 4) {
                    dp[i]--;
                    count--;
                }
            }
        }

        for (int i = 0; i < 5; i++) {
            if (dp[i]) return -1;
        }

        return maxx;
    }
};
