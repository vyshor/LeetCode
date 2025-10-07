class Solution {
public:
    bool checkPerfectNumber(int num) {
        if (num == 1) return false;

        int sq = sqrt(double(num))+1;
        int total = num - 1;
        for (int i = 2; i < sq; i++) {
            if ((num % i) == 0) {
                int other_factor = num / i;
                total -= i + other_factor;
                if (total < 0) return false;
                sq = other_factor;
            }
        }
        return total == 0;
    }
};
