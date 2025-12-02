class Solution {
public:
    int countTrapezoids(vector<vector<int>>& points) {
        constexpr int64_t mod = 1e9 + 7;
        unordered_map<int, int> horizontal_pts;
        for (auto& pt: points) {
            ++horizontal_pts[pt[1]];
        }
        vector<uint64_t> pairs;
        pairs.reserve(horizontal_pts.size());
        uint64_t total{0};
        for (auto [_, v]: horizontal_pts) {
            auto v2 = static_cast<uint64_t>(v);
            int64_t summ = v2*(v2-1) / 2;
            pairs.push_back(summ);
            total += summ;
        }

        uint64_t ans{0};
        for (int64_t p: pairs) {
            total -= p;
            ans = (ans + p * total) % mod;
        }
        return ans;
    }
};
