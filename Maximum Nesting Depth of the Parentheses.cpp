class Solution {
public:
    int maxDepth(string s) {
        int open_count = 0, maxx = 0;
        for (char &c: s) {
            if (c == '(')
                maxx = max(maxx, ++open_count);
            else if (c == ')')
                open_count--;
        }
        return maxx;
    }
};
