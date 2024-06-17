class Solution {
public:
    bool judgeSquareSum(int c) {
        if (!bool(c)) return true;

        unordered_set<uint32_t> dp;
        uint32_t i = 1;
        while (true) {
            uint32_t sq = i*i;
            if (sq == c) return true;
            else if (sq > c) return false;
            dp.insert(sq);
            if (dp.contains(c-sq)) return true;
            i++;
        }
        return false;
    }
};
