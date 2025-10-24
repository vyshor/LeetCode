class Solution {
public:
    int longestBalanced(vector<int>& nums) {
        int n = nums.size();
        int maxx = 0;
        for (int i = 0; i < n-1; i++) {
            int balanced = 0;
            unordered_map<int, int> counter;
            counter[nums[i]]++;
            balanced += 1 + (nums[i] & 1) * -2;
            for (int j = i+1; j < n; j++) {
                counter[nums[j]]++;
                if (counter[nums[j]] == 1) {
                    balanced += 1 + (nums[j] & 1) * -2;
                }

                if (balanced == 0) maxx = max(maxx, j-i+1);
            }
        }
        return maxx;
    }
};
