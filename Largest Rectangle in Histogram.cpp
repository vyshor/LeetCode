class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int maxx = 0;
        int n = heights.size();
        vector<pair<int, int>> stack;
        for (int i = 0; i < n; i++) {
            int h = heights[i];
            maxx = max(maxx, h);
            int earliest_idx = i;
            while (stack.size() > 0 && stack.back().first > h) {
                auto [h2, j] = stack.back();
                // cout << "h2 " << h2 << " j " << j << " i " << i << endl;
                earliest_idx = min(earliest_idx, j);
                stack.pop_back();
                maxx = max(maxx, (i-j)*h2);
            }
            stack.emplace_back(h, earliest_idx);
        }

        int i = n;
        while (stack.size() > 0) {
            auto [h2, j] = stack.back();
            stack.pop_back();
            maxx = max(maxx, (i-j)*h2);
        }
        return maxx;
    }
};
