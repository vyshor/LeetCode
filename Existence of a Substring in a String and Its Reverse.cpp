class Solution {
public:
    bool isSubstringPresent(string s) {
        int n = s.size();
        if (n == 1) return false;

        unordered_set<int> seen;
        for (int i = 1; i < n; ++i) {
            int h1 = ((s[i-1]-97) << 10) | (s[i]-97);
            seen.insert(h1);
        }
        for (int i = 1; i < n; ++i) {
            int h2 = ((s[i]-97) << 10) | (s[i-1]-97);
            if (seen.contains(h2)) return true;
        }
        return false;
    }
};
