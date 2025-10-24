class Solution {
public:
    int smallestNumber(int n) {
        for (int i = 9; i >= 0; i--) {
            if (((n >> i) & 1) == 1) return (1 << (i+1)) - 1;
        }
        return 1;
    }
};
