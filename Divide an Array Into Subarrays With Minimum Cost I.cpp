class Solution {
public:
    int minimumCost(vector<int>& nums) {
        auto comp = greater<int>{};
        make_heap(nums.begin()+1, nums.end(), comp);
        int cost{nums[0]};
        for (int i{0}; i < 2; ++i) {
            pop_heap(nums.begin()+1, nums.end(), comp);
            cost += nums.back();
            nums.pop_back();
        }
        return cost;
    }
};
