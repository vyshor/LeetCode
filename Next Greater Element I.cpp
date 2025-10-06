class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        int m = nums2.size();
        vector<int> ans(n, -1);
        unordered_map<int, int> ref;
        for (int i = 0; i < m; i++) {
            ref[nums2[i]] = i;
        }

        int j = 0;
        for (int num: nums1) {
            int i = ref[num]+1;
            while (i < m) {
                if (nums2[i] > num) {
                    ans[j] = nums2[i];
                    break;
                }
                i++;
            }
            j++;
        }
        return ans;
    }
};
