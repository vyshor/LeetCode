class Solution {
public:
    bool isTrionic(vector<int>& nums) {
        int state{0};
        int count{0};
        int n = nums.size();
        for (int i{1}; i < n; ++i) {
            if (nums[i-1] == nums[i]) return false;

            if (state == 0) {
                if (nums[i-1] < nums[i]) count |= 1;
                else if (count == 0) return false;
                else {
                    state = 1;
                }
            } else if (state == 1) {
                if (nums[i-1] < nums[i]) state = 2;
            } else {
                if (nums[i-1] > nums[i]) return false;
            }
        }
        return state == 2;
    }
};
