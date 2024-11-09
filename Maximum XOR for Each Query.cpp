class Solution {
public:
    vector<int> getMaximumXor(vector<int>& nums, int maximumBit) {
        int xorr = 0, maxx = (1 << maximumBit) - 1, n = nums.size();
        vector<int> ans;
        for (int num: nums) xorr ^= num;
        for (int i = n-1; i > -1; i--) {
            ans.push_back((xorr & maxx) ^ maxx);
            xorr ^= nums[i];
        }
        return ans;
    }
};
