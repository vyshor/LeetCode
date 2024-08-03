class Solution {
public:
    int minSwaps(vector<int>& nums) {
        int k = reduce(nums.begin(), nums.end());
        if (k == 0) return 0;

        int n = nums.size();
        int total = reduce(nums.begin(), nums.begin() + k-1);
        int i = 0, j = k-1;
        int maxx = 0;
        while (i < n) {
            total += nums[j++];
            j %= n;
            maxx = max(maxx, total);
            total -= nums[i++];
        }
        return k - maxx;
    }
};
