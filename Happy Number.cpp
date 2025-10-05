class Solution {
public:
    bool isHappy(int n) {
        vector<int> sq{0, 1, 4, 9, 16, 25, 36, 49, 64, 81};
        unordered_set<int> seen;
        while (n != 1) {
            if (seen.contains(n)) return false;
            seen.insert(n);

            int m = 0;
            while (n > 0) {
                m += sq[n % 10];
                n /= 10;
            }
            n = m;
        }
        return true;

    }
};
