class Solution {
public:
    int finalPositionOfSnake(int n, vector<string>& commands) {
        unordered_map<string, int> movements = {
            {"UP", -n},
            {"DOWN", n},
            {"LEFT", -1},
            {"RIGHT", 1}
        };

        int pos = 0;
        for (string& command: commands) {
            pos += movements[command];
        }
        return pos;
    }
};
