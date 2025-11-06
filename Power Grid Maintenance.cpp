class Solution {
public:
    vector<int> processQueries(int c, vector<vector<int>>& connections, vector<vector<int>>& queries) {
        constexpr int maxN = 100'001;
        bitset<maxN> offline;
        // bitset<maxN> sorted_once;
        vector<int> parents(c+1);
        std::iota(parents.begin(), parents.end(), 0);
        vector<set<int>> q(c+1);

        function<int(int)> find;
        find = [&parents, &find] (int i) -> int {
            if (parents[i] == i) return i;
            int parent = find(parents[i]);
            parents[i] = parent;
            return parent;
        };

        auto uni = [&parents, &find, &q] (int i, int j) {
            int parent_i = find(i);
            int parent_j = find(j);
            if (parent_i == parent_j) return;

            parents[parent_j] = parent_i;
        };

        for (auto& connection: connections) {
            int u = connection[0], v = connection[1];
            uni(u, v);
        }

        for (int i = 1; i < c+1; i++) {
            int parent = find(i);
            q[parent].insert(i);
        }

        vector<int> ans;
        for (auto& query: queries) {
            if (query[0] == 2) {
                int i = query[1];
                offline.set(i);
                int parent = find(i);
                q[parent].erase(i);
            } else {
                int x = query[1];
                if (!offline[x]) {
                    ans.push_back(x);
                    continue;
                }
                int parent = find(x);
                auto& q2 = q[parent];
                // if (!sorted_once[parent]) {
                //     make_heap(q2.begin(), q2.end(), std::greater<>());
                // }

                // while (q2.size() > 0 && offline[q2.front()]) {
                //     pop_heap(q2.begin(), q2.end(), std::greater<>());
                //     q2.pop_back();
                // }

                if (q2.size() > 0) {
                    ans.push_back(*q2.begin());
                } else {
                    ans.push_back(-1);
                }
            }
        }
        return ans;
    }
};
