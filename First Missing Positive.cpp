class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            if (nums[i] > n || nums[i] <= 0) nums[i] = n+1;
        }

        for (int i = 0; i < n; i++) {
            int abs_num = nums[i];
            if (abs_num < 0) abs_num *= -1;
            if (abs_num <= n && nums[abs_num-1] > 0) nums[abs_num-1] *= -1;
        }

        for (int i = 0; i < n; i++) {
            if (nums[i] > 0) return i+1;
        }

        return n+1;
    }
};
