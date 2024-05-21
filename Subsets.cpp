class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> subsets;
        vector<int> arr;
        function<void(int)> explore;
        explore = [&n, &nums, &subsets, &explore, &arr] (int i) -> void {
            if (i == n) {
                vector<int> new_arr = arr;
                subsets.push_back(new_arr);
                return;
            }

            explore(i+1);

            arr.push_back(nums[i]);
            explore(i+1);
            arr.pop_back();
        };
        explore(0);
        return subsets;
    }
};
