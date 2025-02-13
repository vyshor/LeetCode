class Solution {
public:
    pair<int, int> max3(int x0, int x1, int x2) {
        if (x0 <= x1 && x0 <= x2) return {x1, x2};
        if (x1 <= x0 && x1 <= x2) return {x0, x2};
        return {x0, x1};
    }

    int maximumSum(vector<int>& nums) {
        unordered_map<int, pair<int, int>> matches;
        int maxx = -1;
        for (int num: nums) {
            int x = num;
            int summ = 0;
            while (x > 0) {
                summ += x % 10;
                x /= 10;
            }

            if (!matches.contains(summ)) {
                matches[summ] = {num, 0};
            } else {
                matches[summ] = max3(matches[summ].first, matches[summ].second, num);
                maxx = max(maxx, matches[summ].first + matches[summ].second);
            }
        }
        return maxx;
    }
};
