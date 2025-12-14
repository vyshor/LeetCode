class Solution {
public:
    int numberOfWays(string corridor) {
        int n = corridor.size();
        int chairs{0};
        int ch_count{0};
        int pair_state{1};
        vector<int64_t> choices;
        int64_t choice_count{0};
        int64_t count{1};
        int64_t mod = 1e9+7;
        for (int i{0}; i < n; ++i) {
            char ch = corridor[i];
            if (pair_state) {
                ch_count += (ch == 'S');
                // Found both chairs
                if (ch_count == 2) {
                    ch_count = 0;
                    pair_state = 0;
                    choice_count = 1;
                }
            } else {
                if (ch == 'S') {
                    choices.push_back(choice_count);
                    pair_state = 1;
                    ch_count = 1;
                } else {
                    ++choice_count;
                }
            }
            chairs += (ch == 'S');
        }
        if ((chairs & 1) == 1) return 0;
        if (chairs == 0) return 0;

        for (int64_t c: choices) {
            count = (count * c) % mod;
        }
        return count;
    }
};
