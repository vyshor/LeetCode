class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, char> dp;
        set<char> seen;

        if (s.size() != t.size()) return false;

        for (int i = 0; i < s.size(); i++) {
            if (dp.contains(s[i]) && dp[s[i]] != t[i]) return false;

            if (seen.contains(t[i]) && !dp.contains(s[i])) return false;

            dp[s[i]] = t[i];
            seen.insert(t[i]);
        }
        return true;
    }
};
