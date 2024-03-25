class Solution {
public:
    int maxOperations(vector<int>& nums) {
        int i = 2;
        int n = nums.size();
        int summ = nums[0] + nums[1];
        int count = 1;
        while (i+1 < n) {
            if (nums[i] + nums[i+1] == summ) {
                count++;
                i += 2;
            } else
                break;
        }
        return count;
    }
};
