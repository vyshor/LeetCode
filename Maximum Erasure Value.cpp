class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        unordered_map<int, int> prev;
        size_t n = nums.size();
        int summ = 0;
        int maxx = 0;
        int left_ptr = 0;
        for (size_t i = 0; i < n; i++) {
            int num = nums[i];
            if (prev.contains(num)) {
                int idx = prev[num];
                while (left_ptr <= idx) {
                    summ -= nums[left_ptr];
                    left_ptr++;
                }
            }
            summ += num;
            maxx = max(maxx, summ);
            prev[num] = i;
            // cout << "Idx: " << i << " " << maxx << endl;
        }
        return maxx;
    }
};
