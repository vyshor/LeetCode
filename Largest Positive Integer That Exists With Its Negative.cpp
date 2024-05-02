class Solution {
public:
    int findMaxK(vector<int>& nums) {
        unordered_set<int> seen;
        int maxx = -1;
        for (int &num: nums) {
            seen.insert(num);
            if (seen.contains(-num)) {
                if (num < 0) num *= -1;

                maxx = max(maxx, num);
            }
        }
        return maxx;
    }
};
