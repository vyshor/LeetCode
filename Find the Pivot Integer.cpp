class Solution {
public:
    int pivotInteger(int n) {
        if (n==1) return 1;
        int left = 1;
        int right = n;
        int lsum = 0;
        int rsum = 0;
        while (lsum < rsum || left < right-1) {
            lsum += left;
            left++;
            if (lsum > rsum) {
                rsum += right;
                right--;
            }
        }

        if (lsum == rsum && left == right) return left;
        return -1;
    }
};
