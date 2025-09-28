class Solution {
public:
    bool isZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        vector<int> h(n+1, 0);
        for (auto query: queries) {
            int l = query[0], r = query[1];
            h[l]++;
            h[r+1]--;
        }
        int diff = 0;
        for (int i = 0; i < n; i++) {
            diff += h[i];

            if (nums[i] > diff) return false;
        }
        return true;
    }
};