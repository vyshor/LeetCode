class Solution {
public:
    int reverseBits(int n) {
        // std::bitset<32> binary_representation(n);
        // cout << binary_representation << endl;
        int m = 0;
        for (int i = 0; i < 31; i++) {
            m |= (n & 1);
            n >>= 1;
            m <<= 1;
        }
        m |= (n & 1);
        // std::bitset<32> binary_representation2(m);
        // cout << binary_representation2 << endl;
        return m;
    }
};