class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& values) {
        int maxx0 = 0, maxx1 = 0;
        for (int val: values) {
            maxx1 = max(maxx1, val+maxx0-1);
            maxx0 = max(maxx0-1, val);
        }
        return maxx1;
    }
};
