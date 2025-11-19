class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        int count{0};
        for (int num: nums) {
            count += ((num % 3) != 0);
        }
        return count;
    }
};
