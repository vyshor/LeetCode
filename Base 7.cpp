class Solution {
public:
    string convertToBase7(int num) {
        if (num == 0) return "0";
        bool neg = (num < 0);
        if (neg) num = -num;
        stringstream ss;
        while (num > 0) {
            int r = num % 7;
            ss << to_string(r);
            num /= 7;
        }
        if (neg) ss << "-";
        string s = ss.str();
        reverse(s.begin(), s.end());
        return s;
    }
};

class Solution {
public:
    string convertToBase7(int num) {
        stringstream ss;
        if (num < 0) {
            num = -num;
            ss << "-";
        }
        int i = 1;
        while ((num / (i*7)) > 0) {
            i *= 7;
        }
        while (i != 0) {
            ss << to_string(num / i);
            num = num % i;
            i /= 7;
        }

        return ss.str();
    }
};

