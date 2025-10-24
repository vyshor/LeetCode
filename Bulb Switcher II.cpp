class Solution {
public:
    static constexpr int MAX_BITS = 4;

    int flipLights(int n, int presses) {
        vector<int> visited(1 << (MAX_BITS+10), 0);
        int m = MAX_BITS - min(n, MAX_BITS);
        int ans = 0;
        vector<pair<int, int>> q;
        q.emplace_back(0, presses);
        while (q.size() > 0) {
            auto [state, p] = q.back();
            q.pop_back();
            int key = (p << MAX_BITS) | state;

            if (visited[key]) continue;

            visited[key] = 1;
            // cout << "ans=" << ans << " state=" << state << endl;
            if (p == 0) {
                ans++;
                continue;
            }

            int state1 = state ^ (0b1111 >> m);
            int state2 = state ^ (0b1010 >> m);
            int state3 = state ^ (0b0101 >> m);
            int state4 = state ^ (0b1001 >> m);

            vector<int> states = {state1, state2, state3, state4};
            for (int new_state: states) {
                int new_key = ((p-1) << MAX_BITS) | new_state;
                if (!visited[new_key]) q.emplace_back(new_state, p-1);
            }
        }
        return ans;
    }
};
