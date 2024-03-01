class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        int n = s.size();
        int count = 0;
        for (int i=0; i<n; i++) {
            if (s[i] == '1') count++;
        }

        string ns;
        ns.reserve(n);
        stringstream ss(ns);
        n--;
        while (n > 0) {
            if (count > 1) {
                ss << '1';
                count--;
            } else {
                ss << '0';
            }
            n--;
        }
        ss << '1';
        return ss.str();
    }
};
