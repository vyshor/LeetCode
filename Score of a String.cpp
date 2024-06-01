class Solution {
public:
    int scoreOfString(string s) {
        int score = 0, n = s.length(), prev = (int) s[0];

        for (int i = 1; i < n; i++) {
            int current = (int) s[i];
            score += abs(prev-current);
            prev = current;
        }
        return score;
    }
};

