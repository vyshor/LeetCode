class Solution {
public:
    int minOperations(string s) {
        int maxx = 0;
        for (int ch: s) {
            if (ch == 97) continue;
            // b needs 25 ops, 25 ops is max
            maxx = max(maxx, 25-(ch-98));
        }
        return maxx;
    }
};
