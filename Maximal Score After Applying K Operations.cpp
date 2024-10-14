class Solution {
public:
    long long maxKelements(vector<int>& nums, int k) {
        make_heap(nums.begin(), nums.end());
        int64_t score = 0;
        while (k) {
            pop_heap(nums.begin(), nums.end());
            int64_t val = nums.back();
            nums.pop_back();
            score += val;
            val = ceil((double) val / 3.);
            nums.push_back(val);
            push_heap(nums.begin(), nums.end());
            k--;
        }
        return score;
    }
};
