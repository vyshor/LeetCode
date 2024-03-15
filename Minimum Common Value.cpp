class Solution {
public:
    int getCommon(vector<int>& nums1, vector<int>& nums2) {
        int p1 = 0, p2 = 0, n1 = nums1.size(), n2 = nums2.size();
        while (nums1.at(p1) != nums2.at(p2)) {
            while (p1 < n1 && nums1.at(p1) < nums2.at(p2)) p1++;

            if (p1 == n1) return -1;

            while (p2 < n2 && nums2.at(p2) < nums1.at(p1)) p2++;

            if (p2 == n2) return -1;
        }

        if (nums1.at(p1) == nums2.at(p2)) return nums1.at(p1);
        return -1;
    }
};
