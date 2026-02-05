class Solution {
public:
    vector<int> constructTransformedArray(vector<int>& nums) {
        int n = nums.size();
        vector<int> results(n);
        for (int i{0}; i < n; ++i) {
            int val{nums[i]};
            if (val < 0) {
                val += (abs(val) / n + 1) * n;
            }
            results[i] = nums[(val + i) % n];
        }
        return results;
    }
};
