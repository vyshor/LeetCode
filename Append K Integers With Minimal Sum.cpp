class Solution {
public:
    long long minimalKSum(vector<int>& nums, int k) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        int64_t summ = 0;
        int i = 0;
        unordered_set<int> seen;
        while (i < n && nums[i] <= k) {
            if (seen.contains(nums[i])) {
                i++;
                continue;
            }
            seen.insert(nums[i]);

            summ += nums[i];
            i++;
            k++;
        }
        // cout << "n=" << n << " i=" << i << endl;
        // if (i < n) {
        //     cout << "i=" << i << " nums[i]=" << nums[i] << " k=" << k << endl;
        // }
        return (int64_t(k)*int64_t(k+1)/2) - summ;
    }
};
