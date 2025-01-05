class Solution {
public:
    int countPalindromicSubsequence(string s) {
        unordered_map<char, int> last_seen;
        unordered_set<string> ans;
        unordered_set<char> opened;

        int n = s.size();
        for (int i = 0; i < n; i++) {
            last_seen[s[i]] = i;
        }

        for (int i = 0; i < n; i++) {
            char c  = s[i];
            if (i < last_seen[c]) {
                for (char cx: opened) {
                    string h{cx, c};
                    ans.insert(h);
                }

                opened.insert(c);
            } else {
                if (opened.contains(c)) opened.erase(c);

                for (auto cx: opened) {
                    string h{cx, c};
                    ans.insert(h);
                }
            }
        }
        return ans.size();
    }
};
