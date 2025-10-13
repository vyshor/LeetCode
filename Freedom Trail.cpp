class Solution {
public:
    int findRotateSteps(string ring, string key) {
        int n = ring.size();
        int m = key.size();
        unordered_set<int> visited;

        deque<tuple<int, int, int>> q;
        q.emplace_back(0, 0, 0);

        while (q.size() > 0) {
            auto [cost, i, j] = q.front();
            q.pop_front();
            int k = (i << 16) | j;
            if (visited.contains(k)) continue;
            visited.insert(k);

            int x = (i+1) % n;
            int k2 = (x << 16) | j;
            if (!visited.contains(k2)) {
                q.emplace_back(cost+1, x, j);
            }

            x = (i-1+n) % n;
            k2 = (x << 16) | j;
            if (!visited.contains(k2)) {
                q.emplace_back(cost+1, x, j);
            }

            if (ring[i] == key[j]) {
                if (j+1 == m) return cost+1;

                k2 = (i << 16) | (j+1);
                if (!visited.contains(k2)) {
                    q.emplace_back(cost+1, i, j+1);
                }
            }
        }
        return -1;
    }
};
