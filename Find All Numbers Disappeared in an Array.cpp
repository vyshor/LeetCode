class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        int n = nums.size();
        vector<int> seen(n+1);
        for (int num: nums) {
            seen[num] = 1;
        }
        vector<int> ans;
        for (int i = 1; i < n+1; ++i) {
            if (!seen[i]) ans.push_back(i);
        }
        return ans;
    }
};