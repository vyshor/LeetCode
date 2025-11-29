class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        int summ{0};
        for (int num: nums) {
            summ += num;
        }
        return summ % k;
    }
};