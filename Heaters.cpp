class Solution {
public:
    int findRadius(vector<int>& houses, vector<int>& heaters) {
        sort(houses.begin(), houses.end());
        sort(heaters.begin(), heaters.end());

        int m = houses.size();
        int n = heaters.size();
        int i = 0;
        int j = 0;
        int maxx = 0;

        // Special case for left houses
        while (i < m && houses[i] < heaters[j]) {
            maxx = max(maxx, heaters[j]-houses[i]);
            i++;
        }

        while (i < m) {
            while (j+1 < n && heaters[j+1] <= houses[i]) {
                j++;
            }

            int min_dist = houses[i]-heaters[j];
            if (j+1 < n) {
                min_dist = min(min_dist, heaters[j+1]-houses[i]);
            }
            maxx = max(maxx, min_dist);
            i++;
        }
        return maxx;
    }
};
