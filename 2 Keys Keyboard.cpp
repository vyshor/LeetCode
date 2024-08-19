class Solution {
public:
    int minSteps(int n) {
        int steps = 0, i = 2;
        while (n > 1 && i <= n) {
            if (n % i == 0) {
                steps += i;
                n /= i;
                continue;
            } else {
                i++;
            }
        }
        if (n != 1) return steps+n;
        return steps;
    }
};
