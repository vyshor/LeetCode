class Solution {
public:
    int findFinalValue(vector<int>& nums, int original) {
        set<int> seen(nums.begin(), nums.end());
        while (seen.contains(original)) {
            original *= 2;
        }
        return original;
    }
};
