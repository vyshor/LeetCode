class Solution {
public:
    bool isPerfectSquare(int num) {
        if (num == 1) return true;
        // sqrt(2 ** 31 - 1) = 46340
        for (int i = 2; i < min((num >> 1) + 1, 46341); i++) {
            int sq = i*i;
            if (sq == num) return true;
            if (sq > num) return false;
        }
        return false;
    }
};
