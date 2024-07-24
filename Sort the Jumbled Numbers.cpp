class Solution {
public:
    int convert(int i, vector<int>& mapping) {
        if (i == 0) return mapping[i];

        int j = 0, m = 0;
        while (i > 0) {
            j += mapping[(i % 10)] * pow(10, m);
            m++;
            i /= 10;
        }
        return j;
    }
    vector<int> sortJumbled(vector<int>& mapping, vector<int>& nums) {
        vector<vector<int>> arr;
        int n = nums.size();
        arr.reserve(n);
        for (int i = 0; i < n; i++) {
            arr.push_back({convert(nums[i], mapping), i, nums[i]});
        }
        sort(arr.begin(), arr.end());

        vector<int> ans;
        ans.reserve(n);
        for (int i = 0; i < n; i++) {
            ans.push_back(arr[i][2]);
        }
        return ans;
    }
};
