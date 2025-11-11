class Solution {
public:
    int numSub(string s) {
        int64_t MOD = 1e9 + 7;
        int64_t total = 0;
        int64_t count = 0;
        for (char ch: s) {
            if (ch == '1') {
                ++count;
            } else {
                total += (count*(count+1))/2;
                total %= MOD;
                count = 0;
            }
        }
        total += (count*(count+1))/2;
        total %= MOD;
        return total;
    }
};
