class Solution {
public:
    bool rotateString(string s, string goal) {
        if (s.size() != goal.size()) return false;
        s = s+s;
        return s.rfind(goal) != -1;
    }
};
