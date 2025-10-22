class Solution {
public:
    vector<int> createTargetArray(vector<int>& nums, vector<int>& index) {
        int n = nums.size();
        vector<int> ans(n, -1);
        for (int i = n-1; i >= 0; i--) {
            int j = 0;
            int count = index[i];
            while (count > 0) {
                while (ans[j] != -1) j++;
                count--;
                j++;
            }
            while (ans[j] != -1) j++;
            ans[j] = nums[i];
        }
        return ans;
    }
};
