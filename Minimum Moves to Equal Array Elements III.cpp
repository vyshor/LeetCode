class Solution {
public:
    int minMoves(vector<int>& nums) {
        int maxx = nums[0];
        for (int num: nums) {
            maxx = max(maxx, num);
        }

        int count = 0;
        for (int num: nums) {
            count += maxx - num;
        }
        return count;
    }
};
