class Solution {
public:
    bool scoreBalance(string s) {
        int summ = 0;
        int n = s.size();
        for (int ch: s) {
            summ += (ch-96);
        }
        if (summ & 1) return false;
        summ /= 2;

        int csumm = 0;
        for (int i = 0; i < n-1; i++) {
            csumm += (s[i]-96);
            if (csumm == summ) return true;
        }
        return false;
    }
};