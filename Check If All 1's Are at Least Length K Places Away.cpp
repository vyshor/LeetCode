class Solution {
public:
    bool kLengthApart(vector<int>& nums, int k) {
        int n = nums.size();
        int prev_idx = n-1;
        for (int i = 0; i < n; ++i) {
            if (nums[i]) {
                prev_idx = i;
                break;
            }
        }

        for (int i = prev_idx+1; i < n; ++i) {
            if (nums[i]) {
                if (i-prev_idx-1 < k) return false;
                prev_idx = i;
            }
        }
        return true;
    }
};