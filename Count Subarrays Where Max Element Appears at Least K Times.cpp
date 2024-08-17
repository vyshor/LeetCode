class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        int maxx = *max_element(nums.begin(), nums.end());
        vector<int> prefixes, suffixes;
        int count = 0, total = 0;
        for (int i = 0; i < n; i++) {
            count++;
            if (nums[i] == maxx) {
                prefixes.push_back(count);
                count = 0;
                total++;
            }
        }

        if (total < k) return 0;
        for (int i = n-1; i >= 0; i--) {
            if (nums[i] == maxx) suffixes.push_back(n-i);
        }

        int64_t summ = 0;
        for (int i = 0; i < total-k+1; i++){
            summ += (int64_t) prefixes[i] * (int64_t) suffixes[total-k-i];
        }
        return summ;
    }
};
