class Solution {
public:
    bool hasIncreasingSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        if (k == 1) return true;
        vector<int> count(n, 1);
        for (int i = 1; i < n; i++) {
            if (nums[i] > nums[i-1]) {
                count[i] = count[i-1]+1;
                if (count[i] >= k) {
                    if (i-k >= 0 && count[i-k] >= k) return true;
                }
            }
            // cout << "i=" << i << " count: " << count[i] << endl;
        }
        return false;
    }
};
