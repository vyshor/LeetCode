class Solution {
public:
    int countBits(int num) {
        int count = 0;
        while (num > 0) {
            count += num % 2;
            num >>= 1;
        }
        return count;
    }
    bool canSortArray(vector<int>& nums) {
        int n = nums.size();
        int prev_bits = countBits(nums[0]);
        int prev = nums[0], maxx = 0;
        for (int i = 1; i < n; i++) {
            int bits = countBits(nums[i]);
            if (bits == prev_bits) {
                if (nums[i] < maxx) return false;
                prev = max(prev, nums[i]);
                continue;
            } else if (nums[i] < prev) return false;

            maxx = prev;
            prev = max(prev, nums[i]);
            prev_bits = bits;
        }
        return true;
    }
};
