class Solution {
public:
    int longestEqualSubarray(vector<int>& nums, int k) {
        int n = nums.size();
        int maxx = 1;
        unordered_map<int, vector<int>> indexes;
        for (int i = 0; i < n; ++i) {
            indexes[nums[i]].push_back(i);
        }

        for (auto& [_, arr]: indexes) {
            if (arr.size() == 1) continue;

            int left = 0, right = 0;
            int m = arr.size();
            int count = 1;
            while (right < m) {
                while (arr[right]-arr[left]+1-count > k) {
                    --count;
                    ++left;
                }
                maxx = max(maxx, count);
                ++right;
                ++count;
            }
        }
        return maxx;
    }
};
