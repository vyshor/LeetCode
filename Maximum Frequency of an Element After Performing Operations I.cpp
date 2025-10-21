class Solution {
public:
    int maxFrequency(vector<int>& nums, int k, int numOperations) {
        vector<pair<int, int>> diff;
        unordered_map<int, int> counter;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            int num = nums[i];
            diff.emplace_back(-num, 0);
            counter[num]++;
            diff.emplace_back(-num-k-1, -1);
            diff.emplace_back(-num+k, 1);
        }

        int maxx = 0;
        int ops = 0;
        make_heap(diff.begin(), diff.end());
        while (diff.size() > 0) {
            pop_heap(diff.begin(), diff.end());
            auto [num, change] = diff.back();
            diff.pop_back();
            ops += change;

            if (diff.size() == 0 || num != diff.front().first) {
                num = -num;
                // cout << "num: " << num << " ops: " << ops << endl;

                int valid_ops = min(numOperations, ops-counter[num]);
                maxx = max(maxx, valid_ops+counter[num]);
            }
        }
        return maxx;
    }
};
