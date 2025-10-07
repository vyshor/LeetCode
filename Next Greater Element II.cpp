class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n, -1);

        int maxx = *max_element(nums.begin(), nums.end());
        vector<pair<int, int>> stack;
        for (int k = 0; k < 2; k++) {
            for (int i = 0; i < n; i++) {
                int num = nums[i];
                while (stack.size() > 0 && stack.back().first < num) {
                    ans[stack.back().second] = num;
                    stack.pop_back();
                }
                if (num != maxx) {
                    stack.emplace_back(num, i);
                }
            }
        }
        return ans;
    }
};
