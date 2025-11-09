class Solution {
public:
    long long minOperations(vector<int>& nums1, vector<int>& nums2) {
        long long count = 0;
        long long fcount = INT_MAX;
        int n = nums1.size();
        long long fnum = nums2[n];
        for (int i = 0; i < n; i++) {
            count += abs(nums2[i]-nums1[i]);
            if (nums2[i] <= fnum && fnum <= nums1[i]) {
                fcount = 0;
            } else if (nums2[i] >= fnum && fnum >= nums1[i]) {
                fcount = 0;
            } else {
                fcount = min(fcount, abs(fnum-static_cast<long long>(nums2[i])));
                fcount = min(fcount, abs(fnum-static_cast<long long>(nums1[i])));
            }
        }
        return count + fcount + 1;

    }
};
