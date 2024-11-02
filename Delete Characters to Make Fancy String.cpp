class Solution {
public:
    string makeFancyString(string s) {
        int n = s.size();
        if (n <= 2) return s;

        stringstream ss;
        char a = s[0], b = s[1];
        ss << a << b;
        int i = 2;
        while (i < n) {
            char c = s[i++];
            if (c != b || b != a) {
                ss << c;
                a = b;
                b = c;
            }
        }

        return ss.str();
    }
};