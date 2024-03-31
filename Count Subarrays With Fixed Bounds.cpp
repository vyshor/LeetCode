class Solution {
public:
    long long countSubarrays(vector<int>& nums, int minK, int maxK) {
        int n = nums.size();
        int left = 0, right = 0, prev_max = -1, prev_min = -1;
        long long count = 0;
        while (right < n) {
            int num = nums[right];
            if (num > maxK || num < minK) {
                right++;
                left = right;
                prev_max = -1;
                prev_min = -1;
                continue;
            }

            if (num == maxK) prev_max = right;
            if (num == minK) prev_min = right;

            if (prev_max != -1 && prev_min != -1) {
                count += min(prev_max, prev_min)-left+1;
            }
            right++;
        }
        return count;
    }
};

