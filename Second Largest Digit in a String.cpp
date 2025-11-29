class Solution {
public:
    int secondHighest(string s) {
        constexpr char limit{58};
        char maxx{47};
        char maxx2{47};
        for (char ch: s) {
            if (ch <= limit) {
                if (ch == maxx) continue;

                if (ch > maxx) {
                    std::swap(ch, maxx);
                }

                if (ch > maxx2) {
                    std::swap(ch, maxx2);
                }
            }
        }
        if (maxx2 == static_cast<char>(47)) return -1;
        return maxx2 - 48;
    }
};
