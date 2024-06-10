class Solution {
public:
    int heightChecker(vector<int>& heights) {
        vector<int> new_heights = heights;
        sort(new_heights.begin(), new_heights.end());
        int count = 0;
        for (int i = 0; i < heights.size(); i++) {
            count += (new_heights[i] != heights[i]);
        }
        return count;
    }
};