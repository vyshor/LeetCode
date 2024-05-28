class Solution {
public:
    int equalSubstring(string s, string t, int maxCost) {
        int left = 0, right = 0, cost = 0, maxx = 0, n = s.size();
        vector<int> costs;

        while (right < n) {
            costs.push_back(abs((int) (s[right] - t[right])));
            cost += costs[right];

            while (cost > maxCost) {
                cost -= costs[left];
                left++;
            }

            right++;
            maxx = max(maxx, right-left);
        }
        return maxx;
    }
};
