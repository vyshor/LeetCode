class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int val = 0;
        vector<int> bits(32, 0);
        for (int num: nums) {
            for (int i = 0; i < 32; i++) {
                bits[i] += (num & 1);
                num >>= 1;
            }
        }

        int ans = 0;
        for (int i = 0; i < 32; i++) {
            if (bits[i] % 3) ans |= (1 << i);
        }
        return ans;
    }
};
