class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        int i = 0;
        int total = 0;
        vector<pair<int, int>> stack;
        while (i < n) {
            // When climbing out, you need add trapped water
            while (stack.size() > 0 && stack.back().first < height[i]) {
                if (stack.size() > 1) {
                    auto [h, j] = stack.back();
                    auto [h2, j2] = stack[stack.size() - 2];
                    int inc = (min(h2, height[i])-h)*(i-j2-1);
                    total += inc;
                    // cout << "i " << i << " j " << j << " h " << h << " inc " << inc << endl;
                }
                stack.pop_back();
                // cout << "i " << i << " j " << j << " h " << h << " inc " << inc << endl;
            }

            // if (stack.size() > 0) {
            //     auto [h, j] = stack.back();
            //     int inc = (height[i]-h)*(j-i-1);
            //     total += inc;
            // }

            stack.emplace_back(height[i], i);
            i++;
        }
        return total;
    }
};
