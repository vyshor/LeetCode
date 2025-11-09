class Solution {
public:
    int minimumDistance(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int, int> first;
        unordered_map<int, int> second;
        int minn = INT_MAX;
        for (int i = 0; i < n; ++i) {
            int num = nums[i];
            if (first.contains(num)) {
                minn = min(minn, i-first[num]);
            }

            if (second.contains(num)) {
                first[num] = second[num];
            }

            second[num] = i;
        }
        if (minn == INT_MAX) return -1;

        return minn * 2;
    }
};
