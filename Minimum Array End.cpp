class Solution {
public:
    long long minEnd(int n, int x) {
        int64_t ans = 0, shift = 1;
        n--;
        int i = 0;
        while (n > 0 || x > 0) {
            if (x & 1) shift = 1;
            else {
                shift = n & 1;
                n >>= 1;
            }

            ans |= (shift << i++);
            x >>= 1;
        }
        return ans;
    }
};
