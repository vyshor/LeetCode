class Solution {
public:
    int maxAscendingSum(vector<int>& nums) {
        int maxx = nums[0];
        int summ = nums[0];
        int n = nums.size();
        for (int i = 1; i < n; i++) {
            if (nums[i] > nums[i-1]) summ += nums[i];
            else summ = nums[i];
            maxx = max(maxx, summ);
        }
        return maxx;
    }
};