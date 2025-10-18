class Solution {
public:
    int maxDistinctElements(vector<int>& nums, int k) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        int minn = nums[0]-k;
        int count = 0;
        for (int i = 0; i < n; i++) {
            int num = nums[i];
            int curr_min = num-k, curr_max = num+k;
            minn = max(minn, curr_min);
            if (minn <= curr_max) {
                minn++;
                count++;
            }
        }
        return count;
    }
};
