class Solution {
public:
    string predictPartyVictory(string senate) {
        int n = senate.size();
        deque<int> d_alive, r_alive;
        int d_charge = 0, r_charge = 0;

        for (int i = 0; i < n; i++) {
            if (senate[i] == 'D') {
                if (r_charge > 0) {
                    r_charge--;
                } else {
                    d_charge++;
                    d_alive.push_back(i);
                }
            } else {
                if (d_charge > 0) {
                    d_charge--;
                } else {
                    r_charge++;
                    r_alive.push_back(i);
                }
            }
        }

        while (d_alive.size() > 0 && r_charge > 0) {
            d_alive.pop_front();
            r_charge--;
        }

        while (r_alive.size() > 0 && d_charge > 0) {
            r_alive.pop_front();
            d_charge--;
        }

        if (d_alive.size() > 0 && r_alive.size() > 0) {
            stringstream ss;
            while (d_alive.size() > 0 && r_alive.size() > 0) {
                if (d_alive.front() < r_alive.front()) {
                    d_alive.pop_front();
                    ss << 'D';
                } else {
                    r_alive.pop_front();
                    ss << 'R';
                }
            }

            ss << string(d_alive.size(), 'D');
            ss << string(r_alive.size(), 'R');
            return predictPartyVictory(ss.str());
        }

        if (d_alive.size() > 0) return "Dire";
        return "Radiant";
    }
};
