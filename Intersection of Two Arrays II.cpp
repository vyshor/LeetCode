class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        map<int, int> counter;
        for (int num: nums1) {
            counter[num]++;
        }

        vector<int> ans;
        for (int num: nums2) {
            if (counter[num]) {
                counter[num]--;
                ans.push_back(num);
            }
        }
        return ans;
    }
};
