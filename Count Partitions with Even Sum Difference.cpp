class Solution {
public:
    int countPartitions(vector<int>& nums) {
        int summ{0};
        int n = nums.size();
        for (int num: nums) {
            summ ^= num & 1;
        }
        if (summ) return 0;
        return n-1;
    }
};
