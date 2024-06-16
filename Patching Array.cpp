class Solution {
public:
    int minPatches(vector<int>& nums, int n) {
        int i = 0, m = nums.size(), ans = 0;
        uint64_t total = 0, j = 1;
        while (j <= n) {
            while (i < m && nums[i] <= j) {
                total += nums[i++];
            }

            if (total < j) {
                ans++;
                total += j;
            }

            j = total+1;
        }
        return ans;
    }
};
