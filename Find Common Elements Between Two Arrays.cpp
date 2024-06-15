class Solution {
public:
    vector<int> findIntersectionValues(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> counter1;
        unordered_map<int, int> counter2;
        for (int num: nums1) {
            counter1[num]++;
        }

        for (int num: nums2) {
            counter2[num]++;
        }

        int a1 = 0, a2 = 0;
        for (auto [num, count]: counter1) {
            if (counter2.contains(num)) a1 += count;
        }

        for (auto [num, count]: counter2) {
            if (counter1.contains(num)) a2 += count;
        }

        vector<int> ans{a1, a2};
        return ans;
    }
};

