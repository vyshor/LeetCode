class Solution {
public:
    vector<int> avoidFlood(vector<int>& rains) {
        int n = rains.size();
        unordered_map<int, int> prev;
        vector<int> nxt(n, -1);
        vector<int> ans;

        for (int i = 0; i < n; i++) {
            int lake = rains[i];
            if (prev.contains(lake)) {{
                nxt[prev[lake]] = i;
            }}
            prev[lake] = i;
        }

        vector<pair<int,int>> q;
        unordered_set<int> full;
        for (int i = 0; i < n; i++) {
            int lake = rains[i];
            if (lake == 0) {
                if (q.size() > 0) {
                    pop_heap(q.begin(), q.end());
                    auto [_, clear_lake] = q.back();
                    q.pop_back();
                    full.erase(clear_lake);
                    ans.push_back(clear_lake);
                } else {
                    ans.push_back(1);
                }
            } else {
                if (full.contains(lake)) return {};

                if (nxt[i] != -1) {
                    full.insert(lake);
                    q.emplace_back(-nxt[i], lake);
                    push_heap(q.begin(), q.end());
                }

                ans.push_back(-1);
            }
        }
        return ans;
    }
};
