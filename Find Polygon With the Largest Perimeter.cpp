class Solution {
public:
    long long largestPerimeter(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        uint64_t summ = 0;
        for (int i = 0; i < n-1; i++) {
            summ += nums.at(i);
        }

        for (int i = n-1; i > 1; i--) {
            if (summ > nums.at(i)) {
                return summ + nums.at(i);
            } else {
                summ -= nums.at(i-1);
            }
        }
        return -1;
    }
};
