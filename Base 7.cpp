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

