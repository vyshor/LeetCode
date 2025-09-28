class Solution {
public:
    int minTimeToReach(vector<vector<int>>& moveTime) {
        int n = moveTime.size();
        int m = moveTime[0].size();
        vector<tuple<int, int, int>> h;
        unordered_set<int> visited;
        h.emplace_back(0, 0, 1);

        while (h.size() > 0) {
            pop_heap(h.begin(), h.end());
            auto [cost, pos, consume] = h.back();
            h.pop_back();

            if (visited.contains(pos)) continue;
            visited.insert(pos);

            int i = pos >> 10;
            int j = ((1 << 10) - 1) & pos;

            if (i == n-1 && j == m-1) return -cost;
            vector<pair<int, int>>choices{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
            for (auto [x, y]: choices) {
                x += i;
                y += j;
                if (x < 0 || y < 0 || x >= n || y >= m) continue;

                int new_pos = (x << 10) | y;
                if (visited.contains(new_pos)) continue;
                h.emplace_back(min(cost, -moveTime[x][y])-2 + consume, new_pos, consume ^ 1);
                push_heap(h.begin(), h.end());
            }
        }
        return 0;
    }
};
