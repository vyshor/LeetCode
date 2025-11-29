class Solution {
public:
    int movesToMakeZigzag(vector<int>& nums) {
        int n = nums.size();
        int maxx = 0;
        for (int i{0}; i < n; i += 2) {
            int count = 0;
            if (i-1 >= 0) count = max(count, nums[i]-nums[i-1]+1);
            if (i+1 < n) count = max(count, nums[i]-nums[i+1]+1);
            maxx += count;
        }

        int maxx2 = 0;
        for (int i{1}; i < n; i += 2) {
            int count = 0;
            if (i-1 >= 0) count = max(count, nums[i]-nums[i-1]+1);
            if (i+1 < n) count = max(count, nums[i]-nums[i+1]+1);
            maxx2 += count;
        }

        // cout << maxx << " " << maxx2 << endl;

        return min(maxx, maxx2);
    }
};
