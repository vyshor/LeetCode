class Solution {
public:
    int minDays(vector<int>& bloomDay, int m, int k) {
        int n = bloomDay.size();
        if (n / k < m) return -1;

        auto check = [&n, &k, &bloomDay, &m] (int day) -> bool {
            int bouquet = 0, streak = 0;
            for (int i = 0; i < n; i++) {
                if (bloomDay[i] <= day) {
                    if (++streak == k) {
                        streak = 0;
                        if (++bouquet == m) return true;
                    }
                } else {
                    streak = 0;
                }
            }
            return false;
        };

        int left = bloomDay[0], right = bloomDay[0];
        for (int num : bloomDay) {
            left = min(left, num);
            right = max(right, num);
        }
        int minn = right;
        while (left < right) {
            int mid = (left+right)/2;
            if (check(mid)) {
                right = mid;
                minn = min(minn, mid);
            } else {
                if (mid == left) break;
                left = mid;
            }
        }
        return minn;
    }
};
