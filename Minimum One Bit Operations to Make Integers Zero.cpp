class Solution {
public:
    int minimumOneBitOperations(int n) {
        int first_bit = 0;
        int prev = 1;
        for (int i = 31; i >= 0; i--) {
            int mask = (1 << i);
            if (first_bit) {
                n ^= (prev << i);
                prev = (n >> i) & 1;
            } else if (!first_bit && (n & mask) == mask) {
                first_bit = 1;
            }
        }
        return n;
    }
};

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
