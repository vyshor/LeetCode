class Solution {
public:
    long long countBadPairs(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int, int> counter;
        for (int i = 0; i < n; i++) {
            int offset = nums[i]-i;
            counter[offset]++;
        }

        int64_t total_count = (int64_t(n) * int64_t(n-1)) >> 1;
        for (auto [_, count]: counter) {
            total_count -= (int64_t(count) * int64_t(count-1)) >> 1;
        }
        return total_count;
    }
};