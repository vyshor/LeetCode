class Solution {
public:
    int countPalindromicSubsequence(string s) {
        int n = s.size();
        vector<int> first_seen(26, -1);
        vector<int> last_seen(26, -1);

        for (int i{0}; i < n; ++i) {
            int ch = s[i]-97;
            if (first_seen[ch] == -1) first_seen[ch] = i;
            last_seen[ch] = i;
        }

        for (int i{0}; i < 26; ++i) {
            if (first_seen[i] == last_seen[i] && first_seen[i] != -1) {
                first_seen[i] = -1;
                last_seen[i] = -1;
            }
        }

        vector<int> valid_pairs(26*26, 0);
        vector<int> opens(26);
        for (int i{0}; i < n; ++i) {
            int ch = s[i]-97;
            if (last_seen[ch] == i) opens[ch] = 0;
            for (int j{0}; j < 26; ++j) {
                if (opens[j]) {
                    valid_pairs[j*26+ch] = 1;
                }
            }

            if (first_seen[ch] == i) opens[ch] = 1;
        }

        int count = 0;
        for (int i{0}; i < 26*26; ++i) {
            count += valid_pairs[i];
        }
        return count;
    }
};

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
