class Solution {
public:
    int maxSum(vector<int>& nums) {
        int maxx = nums[0];
        unordered_set<int> seen;
        int summ = 0;
        for (int num: nums) {
            if (num > 0) {
                if (!seen.contains(num)) {
                    summ += num;
                    seen.insert(num);
                }
            }
            maxx = max(maxx, num);
        }
        if (seen.size() == 0) return maxx;
        return summ;
    }
};