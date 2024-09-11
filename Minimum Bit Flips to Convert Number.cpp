class Solution {
public:
    int minBitFlips(int start, int goal) {
        int count = 0;
        int val = start ^ goal;
        while (val > 0) {
            count += val % 2;
            val >>= 1;
        }
        return count;
    }
};
