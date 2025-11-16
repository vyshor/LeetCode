class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(2);
        vector<int> seen(n+1);
        for (int num: nums) {
            if (seen[num]) ans[0] = num;
            seen[num] = 1;
        }
        for (int i = 1; i < n+1; ++i) {
            if (!seen[i]) {
                ans[1] = i;
                break;
            }
        }
        return ans;
    }
};
