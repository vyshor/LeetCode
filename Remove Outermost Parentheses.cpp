class Solution {
public:
    string removeOuterParentheses(string s) {
        stringstream ss;
        int open_brackets = 0;
        for (char ch: s) {
            if (ch == '(') {
                if (open_brackets != 0) {
                    ss << ch;
                }
                open_brackets++;
            } else {
                if (open_brackets != 1) {
                    ss << ch;
                }
                open_brackets--;
            }
        }
        return ss.str();
    }
};