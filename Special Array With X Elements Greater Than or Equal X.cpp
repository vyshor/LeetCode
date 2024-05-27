class Solution {
public:
    int specialArray(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            if (i != 0 && nums[i] == nums[i-1]) continue;
            if ((n-i < nums[i] && (i == 0 || nums[i-1] < n-i)) || nums[i] == n-i ) return n-i;
        }
        return -1;
    }
};
