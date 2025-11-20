class Solution {
public:
    vector<bool> prefixesDivBy5(vector<int>& nums) {
        int n = nums.size();
        vector<bool> ans(n);
        ans[0] = nums[0] == 0;
        int remainder = nums[0];
        for (int i{1}; i < n; ++i) {
            remainder = ((remainder*2) % 10)+nums[i];
            ans[i] = ((remainder % 5) == 0);
        }
        return ans;


    }
};
