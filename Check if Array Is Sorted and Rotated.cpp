class Solution {
public:
    bool check(vector<int>& nums) {
        int n = nums.size();
        bool use_rotates = nums[n-1] > nums[0];

        for (int i = 1; i < n; i++) {
            if (nums[i-1] > nums[i]) {
                if (use_rotates) return false;
                use_rotates = true;
            }
        }
        return true;
    }
};
