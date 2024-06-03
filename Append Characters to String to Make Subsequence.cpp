class Solution {
public:
    int appendCharacters(string s, string t) {
        int s1 = 0, t1 = 0, sn = s.size(), tn = t.size();
        while (t1 < tn) {
            while (s1 < sn) {
                if (s[s1] == t[t1]) {
                    s1++;
                    t1++;
                    break;
                } else {
                    s1++;
                }
            }

            if (s1 == sn) return tn-t1;
        }
        return 0;
    }
};
