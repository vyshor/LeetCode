class Solution {
public:
    vector<int> findMissingElements(vector<int>& nums) {
        unordered_set<int> seen;
        int maxx = nums[0], minn = nums[0];
        for (int num: nums) {
            maxx = max(maxx, num);
            minn = min(minn, num);
            seen.insert(num);
        }
        vector<int> ans;
        for (int i = minn+1; i < maxx; i++) {
            if (!seen.contains(i)) ans.push_back(i);
        }
        return ans;
    }
};
