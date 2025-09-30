class Solution {
public:
    bool isUgly(int n) {
        if (n <= 0) return false;
        vector<int> divisors{2,3,5};
        for (int div: divisors) {
            while (n % div == 0) {
                n /= div;
            }
        }
        return n == 1;
    }
};