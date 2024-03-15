class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        set<int> n1(nums1.begin(), nums1.end());
        set<int> n2(nums2.begin(), nums2.end());
        vector<int> ans;
        for (int num: n1) {
            if (n2.contains(num)) ans.push_back(num);
        }
        return ans;
    }
};
