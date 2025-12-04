class Solution {
public:
    int countCollisions(string directions) {
        int ans{0};
        int opens{0};
        int has_s{0};
        for (char ch: directions) {
            if (ch == 'S') {
                if (opens > 0) {
                    ans += opens;
                    opens = 0;
                }
                has_s = 1;
            } else if (ch == 'R') {
                ++opens;
            } else {
                if (opens > 0) {
                    ans += opens+1;
                    opens = 0;
                    has_s = 1;
                } else if (has_s) {
                    ++ans;
                }
            }
            // cout << ans;
        }
        return ans;
    }
};
