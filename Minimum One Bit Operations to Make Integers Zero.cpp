class Solution {
public:
    int minimumOneBitOperations(int n) {
        int binary = n;
        while (n > 0) {
            n >>= 1;
            binary ^= n;
        }
        return binary;
    }
};
