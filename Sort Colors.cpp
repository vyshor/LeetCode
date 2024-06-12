class Solution {
public:
    void sortColors(vector<int>& nums) {
        int n = nums.size();
        int pt0 = 0, pt2 = n-1;
        while (pt2 >= 0 && nums[pt2] == 2) pt2--;
        while (pt0 < n && nums[pt0] == 0) pt0++;
        int pt1 = pt0;

        while (pt1 <= pt2) {
            if (nums[pt1] == 2) {
                swap(nums[pt2], nums[pt1]);
                pt2--;
            } else if (nums[pt1] == 0) {
                if (pt1 == pt0) {
                    pt1++;
                    pt0++;
                } else {
                    swap(nums[pt1], nums[pt0]);
                    pt0++;
                }
            } else {
                pt1++;
            }
        }

    }
};
