class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            nums[i] = abs(nums[i]);
        }
        sort(nums.begin(), nums.end());
        int left = 0, right = n - 1;
        int64_t summ = 0;
        while (left <= right) {
            summ += nums[right]*nums[right];
            right--;

            if (left > right) break;

            summ -= nums[left]*nums[left];
            left++;
        }
        return summ;
    }
};
