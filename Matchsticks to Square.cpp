class Solution {
public:
    vector<int> states;
    vector<int> vals;
    int m;

    void recur(int i, int n, int current_state, uint32_t remaining) {
        // cout << "i " << i << " remaining " << remaining << endl;
        if (i >= n) return;
        uint32_t val = vals[i];

        recur(i+1, n, current_state, remaining);
        if (val > remaining) return;
        if (val == remaining) {
            states.push_back((current_state | (1 << i)));
        } else {
            recur(i+1, n, current_state | (1 << i), remaining-val);
        }
    }

    bool makesquare(vector<int>& matchsticks) {
        vals = matchsticks;
        int n = matchsticks.size();
        uint32_t summ = 0;
        uint32_t maxx = 0;
        for (uint32_t length: matchsticks) {
            summ += length;
            maxx = max(maxx, length);
        }

        if ((summ & 0b11) > 0) return false;
        uint32_t side = summ >> 2;
        if (maxx > side) return false;

        recur(0, n, 0, side);

        int k = states.size();
        // cout << "k: " << k << endl;
        int full_mask = (1 << n) - 1;
        unordered_set<int> seen;
        for (int i = 0; i < k; i++) {
            // const int n2 = 12;
            // cout << "State " << i << " : " <<  std::bitset<n2>(states[i]) << endl;
            for (int j = i+1; j < k; j++) {
                if ((states[i] & states[j]) == 0) {
                    int comb = (states[i] | states[j]);
                    int wanted = full_mask ^ comb;
                    if (seen.contains(wanted)) return true;
                    seen.insert(comb);
                    // cout << "Comb " << i << " " << j << " : " <<  std::bitset<n2>(comb) << endl;
                }
            }
        }
        return false;
    }
};
