class Solution {
public:
    int minimumDeletions(string s) {
        int state_a = 0, state_b = 0;
        for (char c: s) {
            state_b = min(state_a, state_b) + int(c == 'a');
            state_a += int(c == 'b');
        }
        return min(state_a, state_b);
    }
};