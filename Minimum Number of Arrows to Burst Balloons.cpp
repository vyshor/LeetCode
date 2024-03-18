class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        sort(points.begin(), points.end(), [](auto && l, auto && r) { return l.at(1) < r.at(1); });
        int count = 0;
        int prev = 0;
        for (auto& point: points) {
            if (prev >= point.at(0) && count != 0) continue;
            count += 1;
            prev = point.at(1);
        }
        return count;
    }
};
