class Solution {
public:
    unordered_map<int, vector<int>> counter;
    std::mt19937 gen;

    Solution(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            counter[nums[i]].push_back(i);
        }
    }

    int pick(int target) {
        std::uniform_int_distribution<> distrib_int(0, counter[target].size()-1);
        int random_idx = distrib_int(gen);
        return counter[target][random_idx];
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * int param_1 = obj->pick(target);
 */
