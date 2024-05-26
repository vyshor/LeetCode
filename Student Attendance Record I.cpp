class Solution {
public:
    bool checkRecord(string s) {
        int late = 0, absent = 0;
        for (char& c: s) {
            if (c == 'L') {
                late++;
                if (late==3) return false;
            } else {
                late = 0;
                absent += c == 'A';
            }
        }
        return absent <= 1;
    }
};
