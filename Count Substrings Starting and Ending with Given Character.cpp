class Solution {
public:
    long long countSubstrings(string s, char c) {
        int64_t count = 0;
        for (char ch: s) {
            count += c == ch;
        }
        return count*(count+1)/2;
    }
};