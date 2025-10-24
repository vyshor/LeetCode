class Solution {
public:
    int missingMultiple(vector<int>& nums, int k) {
        vector<int> seen(101, 0);
        for (int num: nums) seen[num] = 1;
        int k2 = k;
        while (k2 <= 100 && seen[k2]) k2 += k;
        return k2;
    }
};
