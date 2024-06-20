class Solution {
public:
    int maxDistance(vector<int>& position, int m) {
        sort(position.begin(), position.end());
        int n = position.size();

        auto check = [&position, &m, &n] (int min_dist) -> bool {
            int prev = position[0];
            int baskets = m-1;
            for (int i = 1; i < n; i++) {
                if (position[i]-prev >= min_dist) {
                    baskets--;
                    prev = position[i];
                }
            }
            return baskets <= 0;
        };

        int left = 1, right = (position[n-1]-position[0]) / (m-1) + 1;
        int maxx = 1;
        while (left < right) {
            int mid = (left+right) /2;
            if (check(mid)) {
                maxx = max(maxx, mid);
                if (left == mid) return maxx;
                left = mid;
            } else {
                right = mid;
            }
        }
        return maxx;
    }
};
