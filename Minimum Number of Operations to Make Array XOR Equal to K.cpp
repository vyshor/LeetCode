class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        for (int& num: nums) {
            k ^= num;
        }

        int count = 0;
        while (k > 0)  {
            count += k % 2;
            k >>= 1;
        }
        return count;
    }
};
