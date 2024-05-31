class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int xor1 = 0;
        for (int& num: nums) xor1 ^= num;

        int xor2 = xor1, first_diff = 0;
        while (xor2 % 2 == 0) {
            first_diff++;
            xor2 >>= 1;
        }

        xor2 = 0;
        for (int& num: nums) {
            if (((1 << first_diff) & num) > 0) xor2 ^= num;
        }
        xor1 ^= xor2;
        return {xor1, xor2};
    }
};
