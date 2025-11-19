class Solution {
public:
    int findFinalValue(vector<int>& nums, int original) {
        vector<int> seen(1001, 0);
        for (int num: nums) seen[num] = 1;
        while (original <= 1000 && seen[original]) {
            original *= 2;
        }
        return original;
    }
};

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
