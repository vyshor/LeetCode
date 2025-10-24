class Solution {
public:
    bool judgeCircle(string moves) {
        int xpos = 0, ypos = 0;
        int n = moves.size();
        for (int i = 0; i < n; i++) {
            if (moves[i] == 'R') xpos++;
            else if (moves[i] == 'L') xpos--;
            else if (moves[i] == 'U') ypos++;
            else ypos--;
        }
        return xpos == 0 && ypos == 0;
    }
};