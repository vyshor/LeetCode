class Solution {
public:
    bool canBeValid(string s, string locked) {
        int n = s.size();
        if (n % 2) return false;

        int opens = 0, unlocked = 0;
        for (int i = 0; i < n; i++) {
            if (locked[i] == '1') {
                if (s[i] == '(') {
                    opens++;
                } else {
                    if (opens >= 1) {
                        opens--;
                    } else if (unlocked >= 1) {
                        unlocked--;
                    } else {
                        return false;
                    }
                }
            } else {
                unlocked++;
            }
        }

        opens = 0;
        unlocked = 0;
        for (int i = n-1; i >= 0; i--) {
            if (locked[i] == '1') {
                if (s[i] == ')') {
                    opens++;
                } else {
                    if (opens >= 1) {
                        opens--;
                    } else if (unlocked >= 1) {
                        unlocked--;
                    } else {
                        return false;
                    }
                }
            } else {
                unlocked++;
            }
        }
        return true;
    }
};
