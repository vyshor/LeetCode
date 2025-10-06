class Solution {
public:
    vector<int> constructRectangle(int area) {
        int sq = sqrt(double(area))+1;
        int maxx = 1;
        for (int i = 2; i < sq; i++) {
            if (area % i == 0) {
                maxx = i;
                sq = (area / maxx) + 1;
            }
        }
        if (maxx == 1) return {area, 1};
        return {maxx, area / maxx};
    }
};