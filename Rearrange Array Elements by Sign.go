class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        int n = nums.size();
        vector<int> arr;
        arr.reserve(n);
        int i = 0;
        int j = 0;
        bool pos = true;
        while (nums[i] < 0) {
            i++;
        }
        while (nums[j] > 0) {
            j++;
        }

        while (i < n || j < n) {
            if (pos) {
                arr.push_back(nums[i++]);
                while (i < n && nums[i] < 0) {
                    i++;
                }
            } else {
                arr.push_back(nums[j++]);
                while (j < n && nums[j] > 0) {
                    j++;
                }
            }
            pos = !pos;
        }
        return arr;
    }
};
