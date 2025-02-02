class Solution {
public:
    bool isArraySpecial(vector<int>& nums) {
        int n = nums.size();
        int parity = nums[0] & 1;
        for (int i = 1; i < n; i++) {
            int new_parity = nums[i] & 1;
            if (parity == new_parity) return false;
            parity = new_parity;
        }
        return true;
    }
};
