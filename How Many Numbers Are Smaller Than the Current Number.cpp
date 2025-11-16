class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        int n = nums.size();
        vector<pair<int, int>> arr(n);
        for (int i = 0; i < n; ++i) {
            arr[i].first = nums[i];
            arr[i].second = i;
        }
        sort(arr.begin(), arr.end());

        nums[arr[0].second] = 0;
        for (int i = 1; i < n; ++i) {
            if (arr[i].first > arr[i-1].first) {
                nums[arr[i].second] = i;
            } else {
                nums[arr[i].second] = nums[arr[i-1].second];
            }
        }
        return nums;
    }
};
