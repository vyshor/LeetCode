class Solution {
public:
    long long maximumValueSum(vector<int>& nums, int k, vector<vector<int>>& edges) {
        int msb = -1, i = k;
        while (i > 0) {
            msb++;
            i >>= 1;
        }

        int msb_count = 0, n = nums.size();
        int64_t max_msb = 1 << msb, mask = (1 << (msb+1))-1, total = 0;
        int64_t minn = mask << 1, mask_total = 0;

        for (int64_t num : nums) {
            int64_t i =  num & mask;
            total += num ^ i;
            if (i < max_msb) i ^= k;
            else msb_count++;

            minn = min(minn, i - (i ^k));
            mask_total += i;
        }

        int non_msb_count = n - msb_count;
        if (non_msb_count % 2) return total + mask_total - minn;
        return total + mask_total;
    }
};
