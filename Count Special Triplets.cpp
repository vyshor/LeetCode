class Solution {
public:
    int specialTriplets(vector<int>& nums) {
        constexpr int64_t mod = 1e9+7;
        int64_t count = 0;
        unordered_map<int, int64_t> left_counter;
        unordered_map<int, int64_t> right_counter;
        for (int num: nums) {
            ++right_counter[num];
        }
        for (int num : nums) {
            --right_counter[num];
            int val = num*2;
            if (left_counter.contains(val) && right_counter.contains(val)) {
                count = (count + left_counter[val] * right_counter[val]) % mod;
            }
            ++left_counter[num];
        }
        return count;
    }
};
