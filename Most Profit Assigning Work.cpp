class Solution {
public:
    int maxProfitAssignment(vector<int>& difficulty, vector<int>& profit, vector<int>& worker) {
        vector<pair<int, int>> q;
        int n = profit.size();
        int min_difficulty = 1 << 17;
        int max_profit = 0;
        for (int i = 0; i < n; i++) {
            min_difficulty = min(min_difficulty, difficulty[i]);
            max_profit = max(max_profit, profit[i]);
            q.emplace_back(difficulty[i], -profit[i]);
        }

        sort(q.begin(), q.end());
        int maxx = 0;
        for (int i = 0; i < n; i++) {
            maxx = min(maxx, q[i].second);
            q[i].second = maxx;
        }

        int total = 0;
        for (int w : worker) {
            if (w < min_difficulty) continue;
            auto lower = lower_bound(q.begin(), q.end(), make_pair(w, -max_profit));
            if (lower != q.end() && lower->first == w) total -= lower->second;
            else total -= (lower-1)->second;
        }
        return total;
    }
};
