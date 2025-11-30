class Solution {
public:
    int minSubarray(vector<int>& nums, int p) {
        int n = nums.size();
        int r = 0;
        for (int num: nums) {
            r += num;
            r %= p;
        }
        if (r == 0) return 0;

        unordered_map<int, int> seen;
        seen[0] = -1;
        int summ = 0;
        int minn = n+1;
        for (int i{0}; i < n; ++i) {
            summ += nums[i];
            summ %= p;
            int k = (summ - r + p) % p;
            // cout << "k:" << k << " summ:" << summ << endl;
            if (seen.contains(k)) {
                minn = min(minn, i-seen[k]);
            }
            seen[summ] = i;
        }
        if (minn >= n) return -1;
        return minn;
    }
};
