class Solution {
public:
    bool checkValidString(string s) {
        int lo = 0, hi = 0;
        for (char &c : s) {
            switch (c) {
                case '(':
                    lo++;
                    hi++;
                    break;
                case ')':
                    lo = max(lo-1, 0);
                    if (--hi < 0) return false;
                    break;
                default:
                    lo = max(lo-1, 0);
                    hi++;
            }
        }
        return (lo == 0);
    }
};

