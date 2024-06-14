class Solution {
public:
    int minIncrementForUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int minn = nums[0], count = 0;
        for (int& num: nums) {
            minn = max(minn, num);
            if (num < minn) {
                count += minn - num;
            }
            minn++;
        }
        return count;
    }
};
