class Solution {
public:
    int findComplement(int num) {
        int i = 0, ans = 0;
        while (num > 0) {
            if (num % 2 == 0) ans |= (1 << i);
            i++;
            num >>= 1;
        }
        return ans;
    }
};
