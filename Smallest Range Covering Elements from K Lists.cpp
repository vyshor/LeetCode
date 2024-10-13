class Solution {
public:
    vector<int> smallestRange(vector<vector<int>>& nums) {
        vector<vector<int>> q;
        int maxx = nums[0][0];
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            maxx = max(maxx, nums[i][0]);
            q.push_back({-nums[i][0], i, 0});
        }

        make_heap(q.begin(), q.end());
        int minn = maxx + q[0][0];
        vector<int> ans{-q[0][0], maxx};

        while (1) {
            if (maxx + q[0][0] < minn) {
                minn = maxx + q[0][0];
                ans = {-q[0][0], maxx};
            }

            pop_heap(q.begin(), q.end());
            auto v = q.back();
            q.pop_back();
            int i = v[1], j = v[2];
            if (j+1 == nums[i].size()) return ans;

            q.push_back({-nums[i][j+1], i, j+1});
            push_heap(q.begin(), q.end());
            maxx = max(maxx, nums[i][j+1]);
        }
    }
};