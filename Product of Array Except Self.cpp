class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp_left(n,1);
        vector<int> dp_right(n,1);
        int left = 1;
        for (int i = 0; i < n; i++) {
            left *= nums.at(i);
            dp_left.at(i) = left;
        }

        int right = 1;
        for (int i = n-1; i >= 0; i--) {
            right *= nums.at(i);
            dp_right.at(i) = right;
        }

        vector<int> ans(n, 1);
        for (int i = 0; i<n; i++) {
            int val = 1;
            if (i+1 < n) val *= dp_right.at(i+1);
            if (i-1 >= 0) val *= dp_left.at(i-1);
            ans.at(i) = val;
        }

        return ans;
    }
};