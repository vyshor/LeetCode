class Solution {
public:
    int getState(char c) {
        switch (c) {
            case '.':
            return 0;
            case 'L':
            return -1;
            default:
            return 1;
        }
    }

    char statestr(int i) {
        switch (i) {
            case 1:
            return 'R';
            case -1:
            return 'L';
            default:
            return '.';
        }
    }

    string pushDominoes(string dominoes) {
        int n = dominoes.size();
        vector<int> states(n, 0);
        vector<int> last(n, n);
        deque<tuple<int, int, int>> q;
        for (int i = 0; i < n; i++) {
            int state = getState(dominoes[i]);
            if (state != 0) {
                q.emplace_back(i, state, 0);
            }
        }

        while (q.size() > 0) {
            auto [pos, state, turn] = q.front();
            // cout << "Pos: " << pos << " State: " << state << " Turn: " << turn << endl;
            q.pop_front();
            if (turn == last[pos]) {
                states[pos] += state; // Breakeven state
            } else if (turn - last[pos] >= 1) {
                continue; // Consumed state
            } else {
                states[pos] += state;
                last[pos] = turn;
                if (pos+state >= 0 && pos+state < n) {
                    q.emplace_back(pos+state, state, turn+1);
                }
            }
        }

        for (int i = 0; i < n; i++) {
            dominoes[i] = statestr(states[i]);
        }
        return dominoes;
    }
};
