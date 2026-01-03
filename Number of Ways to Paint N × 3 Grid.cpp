class Solution {
public:
    int numOfWays(int n) {
        constexpr int64_t mod = 1e9+7;
        vector<int64_t> states(12, 1);
        for (int i{1}; i < n; ++i) {
            vector<int64_t> new_states(12);
            new_states[0] = states[4] + states[5] + states[7] + states[8] + states[9];
            new_states[1] = states[4] + states[6] + states[7] + states[8];
            new_states[2] = states[4] + states[5] + states[8] + states[9] + states[11];
            new_states[3] = states[5] + states[9] + states[10] + states[11];

            new_states[4] = states[0] + states[1] + states[2] + states[10] + states[11];
            new_states[5] = states[0] + states[2] + states[3] + states[10];
            new_states[6] = states[1] + states[8] + states[9] + states[11];
            new_states[7] = states[0] + states[1] + states[9] + states[10] + states[11];

            new_states[8] = states[0] + states[1] + states[2] + states[6];
            new_states[9] = states[0] + states[2] + states[3] + states[6] + states[7];
            new_states[10] = states[3] + states[4] + states[5] + states[7];
            new_states[11] = states[2] + states[3] + states[4] + states[6] + states[7];

            for (int j{0}; j < 12; ++j) {
                new_states[j] %= mod;
            }

            states.swap(new_states);
        }

        int64_t summ{0};
        for (int j{0}; j < 12; ++j) {
            summ += states[j];
            summ %= mod;
        }
        return summ;
    }
};
