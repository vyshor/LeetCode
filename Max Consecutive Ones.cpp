class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int maxx = 0;
        int count = 0;
        for (int num: nums) {
            int digit = num & 1;
            count = (count + digit) * digit;
            maxx = max(maxx, count);
        }
        return maxx;
    }
};
