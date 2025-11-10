class Solution {
public:
    int minOperations(vector<int>& nums) {
        vector<int> stack = {0};
        int count = 0;
        for (int num: nums) {
            while (stack.back() > num) {
                stack.pop_back();
            }
            if (stack.back() != num) {
                stack.push_back(num);
                ++count;
            }
        }
        return count;
    }
};
