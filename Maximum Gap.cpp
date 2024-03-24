class Solution {
public:
    int maximumGap(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        if (n < 2) return 0;
        int maxx = -1;
        for (int i = 1; i<n; i++) {
            maxx = max(maxx, nums.at(i)-nums.at(i-1));
        }
        return maxx;
    }
};

