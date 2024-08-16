class Solution {
public:
    int maxDistance(vector<vector<int>>& arrays) {
        int minn0 = INT_MAX, minn1 = INT_MAX, maxx0 = INT_MIN, maxx1 = INT_MIN;
        int i0 = 0, i1 = 0, j0 = 0, j1 = 0;
        int n = arrays.size();
        for (int i = 0; i < n; i++) {
            if (arrays[i][0] < minn0) {
                minn1 = minn0;
                minn0 = arrays[i][0];
                i1 = i0;
                i0 = i;
            } else if (arrays[i][0] < minn1) {
                minn1 = arrays[i][0];
                i1 = i;
            }

            if (arrays[i].back() > maxx0) {
                maxx1 = maxx0;
                maxx0 = arrays[i].back();
                j1 = j0;
                j0 = i;
            } else if (arrays[i].back() > maxx1) {
                maxx1 = arrays[i].back();
                j1 = i;
            }
        }

        if (i0 == j0) return max(maxx0-minn1, maxx1-minn0);
        return maxx0 - minn0;
    }
};
