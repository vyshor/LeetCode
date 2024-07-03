class Solution {
public:
    int minDifference(vector<int>& nums) {
        int n = nums.size();
        if (n <= 4) return 0;

        sort(nums.begin(), nums.end());
        int left = 0, right = n-1;
        return min({nums[right-3]-nums[left], nums[right-2]-nums[left+1], nums[right-1]-nums[left+2], nums[right]-nums[left+3]});
    }
};