class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> ans;
        int n = nums.size();
        for (int num: nums) {
            num %= n;
            if (num == 0) num = n;
            if (nums[num-1] > n) ans.push_back(num);
            else nums[num-1] += n;
        }
        return ans;
    }
};
