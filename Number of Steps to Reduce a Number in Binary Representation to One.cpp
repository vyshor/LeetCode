class Solution {
public:
    int numSteps(string s) {
        int n = s.size(), carry_over = 0, steps = 0;
        int i = n-1;
        while (i > 0) {
            if ((s[i] == '1' && carry_over == 0) || (s[i] == '0' && carry_over)) {
                steps += 2;
                carry_over = 1;
            } else {
                steps++;
                carry_over = s[i] == '1';
            }
            i--;
        }
        return steps + carry_over;
    }
};
