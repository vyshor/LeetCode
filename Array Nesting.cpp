class Solution {
public:
    int arrayNesting(vector<int>& nums) {
        int n = nums.size();

        int maxx = 1;
        for (int i = 0; i < n; i++) {
            if (nums[i] == -1) continue;

            int prev_idx = i;
            int val = nums[i];
            // cout << "val: " << val << endl;
            nums[i] = -1;
            int count = 1;
            while (val != i) {
                // cout << prev_idx << endl;
                nums[prev_idx] = -1;
                prev_idx = val;
                val = nums[val];
                count++;
            }
            nums[prev_idx] = -1;
            maxx = max(maxx, count);
            if (maxx >= ((n+1) / 2)) return maxx;
        }
        return maxx;

    }
};
