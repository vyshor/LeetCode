class Solution {
public:
    int minScore(int n, vector<vector<int>>& roads) {
        vector<int> parents(n+1);
        vector<int> minn(n+1, INT_MAX);
        std::iota(parents.begin(), parents.end(), 0);

        function<int(int i)> ffind;
        ffind = [&parents, &ffind] (int i) -> int {
            if (parents[i] == i) return i;
            int parent = ffind(parents[i]);
            parents[i] = parent;
            return parent;
        };

        auto uni = [&parents, &minn, &ffind] (int parent_i, int j) {
            int parent_j = ffind(j);
            if (parent_i != parent_j) {
                parents[parent_j] = parent_i;
                minn[parent_i] = min(minn[parent_i], minn[parent_j]);
            }
        };

        for (auto& road: roads) {
            int a = road[0], b = road[1], dist = road[2];
            int parent_a = ffind(a);

            minn[parent_a] = min(minn[parent_a], dist);
            uni(parent_a, b);
        }
        return minn[ffind(1)];
    }
};