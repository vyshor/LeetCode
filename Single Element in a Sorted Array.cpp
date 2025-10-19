class Solution {
public:
    vector<int> NUMS;

    int recur(int i, int j) {
        if (i == j) return NUMS[i];
        int mid = (i+j)/2;
        int below_val = NUMS[mid-1], mid_val = NUMS[mid], above_val = NUMS[mid+1];
        if (mid_val != below_val && mid_val != above_val) return mid_val;

        int left_count = mid-i, right_count=j-mid;
        int left_border = mid-1, right_border=mid+1;
        if (above_val == mid_val) {
            right_count--;
            right_border++;
        } else {
            left_count--;
            left_border--;
        }

        if (right_count & 1) {
            return recur(right_border, j);
        } else {
            return recur(i, left_border);
        }
    }
    int singleNonDuplicate(vector<int>& nums) {
        int n = nums.size();
        NUMS = std::move(nums);
        return recur(0, n-1);
    }
};
